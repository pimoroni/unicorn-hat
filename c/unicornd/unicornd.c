/*
 * Copyright (C) 2014 jibi <jibi@paranoici.org>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <string.h>
#include <signal.h>

#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>

#include <ws2812-RPi.h>

#define SOCK_PATH "/var/run/unicornd.socket"

#define	UNICORND_CMD_SET_BRIGHTNESS 0
#define	UNICORND_CMD_SET_PIXEL      1
#define	UNICORND_CMD_SET_ALL_PIXELS 2
#define	UNICORND_CMD_SHOW           3

#define recv_or_return(socket, buf, len, flags) \
{                                               \
	int _ret;                               \
	_ret = recv(socket, buf, len, flags);   \
                                                \
	if (_ret <= 0) {                        \
		close(socket);                  \
		return;                         \
	}                                       \
}

typedef struct col_s {
	uint8_t r;
	uint8_t g;
	uint8_t b;
} __attribute__ ((packed)) col_t;

typedef struct pos_s {
	uint8_t x;
	uint8_t y;
} __attribute__ ((packed)) pos_t;

static void
unicornd_exit(int status)
{
	int i;

	for (i = 0; i < 64; i++) {
		setPixelColor(i,0,0,0);
	}

	show();
	terminate(status);
}

static int
get_pixel_pos(uint8_t x, uint8_t y)
{
	int map[8][8] = {
		{7 ,6 ,5 ,4 ,3 ,2 ,1 ,0 },
		{8 ,9 ,10,11,12,13,14,15},
		{23,22,21,20,19,18,17,16},
		{24,25,26,27,28,29,30,31},
		{39,38,37,36,35,34,33,32},
		{40,41,42,43,44,45,46,47},
		{55,54,53,52,51,50,49,48},
		{56,57,58,59,60,61,62,63}
	};

	return map[x][y];
}

static
void
init_unicorn_hat(void)
{
	int i;
	struct sigaction sa;

	numLEDs = 64;
	initHardware();
	clearLEDBuffer();
	setBrightness(DEFAULT_BRIGHTNESS);

	for (i = 0; i < 64; i++) {
		memset(&sa, 0, sizeof(sa));
		sa.sa_handler = unicornd_exit;
		sigaction(i, &sa, NULL);
	}
}

static
int
setup_listen_socket(void)
{
	int listen_socket;
	int ret;
	socklen_t len;
	struct sockaddr_un local;

	listen_socket = socket(AF_UNIX, SOCK_STREAM, 0);
	if (listen_socket == -1) {
		fprintf(stderr, "cannot create unix socket");
		exit(1);
	}

	unlink(SOCK_PATH);

	local.sun_family = AF_UNIX;
	strcpy(local.sun_path, SOCK_PATH);
	len = strlen(local.sun_path) + sizeof(local.sun_family);

	ret = bind(listen_socket, (struct sockaddr *) &local, len);
	if (ret == -1) {
		fprintf(stderr, "cannot bind socket");
		exit(1);
	}

	ret = listen(listen_socket, 4);
	if (ret == -1) {
		fprintf(stderr, "cannot listen on socket");
		exit(1);
	}

	return listen_socket;
}

static
int
do_accept(int listen_socket) {
	struct sockaddr_un client;
	int client_socket;
	socklen_t len;

	len = sizeof(client);

	client_socket = accept(listen_socket, (struct sockaddr *)&client, &len);
	if (client_socket == -1) {
		fprintf(stderr, "cannot accept client connection");
		exit(1);
	}

	return client_socket;
}

static
void
handle_client(int client_socket) {
	uint8_t cmd;

	double bright;

	pos_t pos;
	col_t col;

	col_t pixels[64];
	
	int x, y;

	while (true) {
		recv_or_return(client_socket, &cmd, sizeof(char), 0);

		switch (cmd) {
			case UNICORND_CMD_SET_BRIGHTNESS:

				recv_or_return(client_socket, &bright, sizeof(double), 0);

				setBrightness(bright);
				break;

			case UNICORND_CMD_SET_PIXEL:

				recv_or_return(client_socket, &pos, sizeof(pos_t), 0);
				recv_or_return(client_socket, &col, sizeof(col_t), 0);

				setPixelColor(get_pixel_pos(pos.x, pos.y), col.r, col.g, col.b);
				break;

			case UNICORND_CMD_SET_ALL_PIXELS:
				recv_or_return(client_socket, &pixels, 64 * sizeof(col_t), 0);

				for (x = 0; x < 8; x++) {
					for (y = 0; y < 8; y++) {
						col_t *col = &pixels[x * 8 + y];
						setPixelColor(get_pixel_pos(x, y), col->r, col->g, col->b);
					}
				}

				break;

			case UNICORND_CMD_SHOW:

				show();
				break;

			default:

				close(client_socket);
				return;
		}
	}
}

int
main(void)
{
	int listen_socket, client_socket;

	init_unicorn_hat();
	listen_socket = setup_listen_socket();

	while (true) {
		client_socket = do_accept(listen_socket);

		if (client_socket != -1) {
			handle_client(client_socket);
		}
	}

	return 0;
}


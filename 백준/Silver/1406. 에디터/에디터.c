#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100010

typedef struct _DATA {
	char data;
	struct _DATA *former;
	struct _DATA *next;
} DATA;

DATA* mk_link(char arr[MAX + 1], DATA *start);
DATA* add(DATA *now, const char should_add);
DATA* del(DATA *now);

int main() {
	int num, i;
	char arr[MAX + 1] = { 0 }, temp[5] = { 0 };
	DATA *start, *now, *next;
	start = (DATA *)malloc((sizeof(DATA)));

	scanf("%s", arr);

	now = mk_link(arr, start);

	scanf("%d", &num);
	fgets(temp, 5, stdin); // 줄바꿈 삭제

	for (i = 0; i < num; i++) {
		fgets(temp, 5, stdin); // 줄바꿈

		if (temp[0] == 'L' && now != start) {
			now = now->former; // 왼쪽 이동
		} else if (temp[0] == 'D' && now->next != NULL) {
			now = now->next; // 오른쪽 이동
		} else if (temp[0] == 'B' && now != start) {
			now = del(now); // 현재 커서 지우기, 왼쪽 것을 현재 커서로 설정
		} else if (temp[0] == 'P') {
			now = add(now, temp[2]); // 추가, 추가된 것을 현재 커서로
		}
	}

	now = start->next;
	while (now != NULL) {
		printf("%c", now->data);
		next = now->next;
		free(now);
		now = next;
	}
    free(start);
	return 0;
}

DATA* mk_link(char arr[MAX + 1], DATA *start) {
	int i, length;
	DATA *former, *next, *now;

	length = strlen(arr);

	former = start;
	now = (DATA *)malloc(sizeof(DATA));
	start->next = now;

	for (i = 0; i < length; i++) {
		if (i == length - 1) {
			next = NULL;
		} else {
			next = (DATA *)malloc(sizeof(DATA));
		}
		now->data = arr[i];
		now->former = former;
		now->next = next;
		former = now; // 마지막에 return해야 할 것
		now = next; // 마지막에는 NULL이 됨
	}

	return former;
}

DATA* add(DATA *now, const char should_add) {
	DATA *new = (DATA *)malloc(sizeof(DATA));
	new->former = now;
	new->next = now->next;
	now->next = new;
	if (new->next != NULL) {
		new->next->former = new;
	}
	new->data = should_add;

	return new;
}

DATA* del(DATA *now) {
	DATA *temp = now->former;
	now->former->next = now->next;
    if (now->next != NULL) {
        now->next->former = now->former;
    }
	free(now);

	return temp;
}
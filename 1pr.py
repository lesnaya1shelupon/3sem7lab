#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import os.path
import argparse


def add_people(list_people, surname, name, post, datta):
    """
    Добавить данные магазина.
    """
    list_people.append(
        {
            "surname": surname,
            "name": name,
            "post": post,
            "datta": datta
        }
    )
    return list_people


def display_table(list_people):
    if list_people:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 15,
            '-' * 30,
            '-' * 20,
            '-' * 15
        )
        print(line)

        print('| {:^4} | {:^15} | {:^30} | {:^20} | {:^15} | '.format(
            "№",
            "Дата рождения",
            "Фамилия",
            "Имя",
            "Знак Зодиака"
           )
        )

        print(line)

        for idx, spisok_new_new in enumerate(list_people, 1):
            print(
                '| {:>4} | {:<15} | {:<30} | {:<20} | {:<15} | '.format(
                    idx,
                    spisok_new_new.get('datta', ''),
                    spisok_new_new.get('surname', ''),
                    spisok_new_new.get('name', ''),
                    spisok_new_new.get('post', 0)
                )
            )
        print(line)
    else:
        print("Список людей пуст.")


def select_zodiac(list_people, post_sear):
    search_post = []
    for post_sear_itme in list_people:
        if post_sear == post_sear_itme['post']:
            search_post.append(post_sear_itme)
    return search_post


def save_people(file_name, list_people):
    with open(file_name, 'w', encoding="utf-8") as fout:
        json.dump(list_people, fout, ensure_ascii=False, indent=4)


def load_list_people(file_name):
    with open(file_name, 'r', encoding="utf-8") as fin:
        return json.load(fin)


def main(command_line=None):
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
        help="The datta file name"
    )

    parser = argparse.ArgumentParser("zodiac")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser(
        "add",
        parents=[file_parser],
        help="Add a new people"
    )

    add.add_argument(
        "-sn",
        "--surname",
        action="store",
        required=True,
        help="The peoples' surname"
    )

    add.add_argument(
        "-n",
        "--name",
        action="store",
        required=True,
        help="The peoples' name"
    )

    add.add_argument(
        "-p",
        "--post",
        action="store",
        required=True,
        help="The peoples' zodiac sign"
    )

    add.add_argument(
        "-dt",
        "--datta",
        action="store",
        type=int,
        required=True,
        help="Date of Birth"
    )

    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
        help="Display all peoples"
    )

    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
        help="Select the zodiac"
    )

    select.add_argument(
        "-PS",
        "--post_sear",
        action="store",
        type=str,
        required=True,
        help="The find zodiac"
    )

    args = parser.parse_args(command_line)
    is_dirty = False
    if os.path.exists(args.filename):
        people = load_list_people(args.filename)
    else:
        people = []
    if args.command == "add":
        people = add_people(
            people,
            args.surname,
            args.name,
            args.post,
            args.datta
        )
        is_dirty = True
    elif args.command == "display":
        display_table(people)

    elif args.command == "select":
        selected = select_zodiac(people, args.post_sear)
        display_table(selected)

    if is_dirty:
        save_people(args.filename, people)


if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""A script that uses REST API for employees todo list"""

from requests import get
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = get(url)
    username = response.json().get('username')

    listUrl = url + "/todos"
    response = get(listUrl)
    tasks = response.json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for i in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, username, i.get('completed'),
                               i.get('title')))

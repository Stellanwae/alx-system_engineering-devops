#!/usr/bin/python3
"""Script that use REST API to print employee id"""

import sys
from requests import get


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = get(todoUrl)
    tasks = response.json()
    done = 0
    completed = []

    for i in tasks:
        if i.get('completed'):
            completed.append(i)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for i in completed:
        print("\t {}".format(i.get('title')))

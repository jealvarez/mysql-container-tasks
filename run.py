#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import subprocess
import sys
import argparse

def execute():
  process = subprocess.Popen('ansible-playbook playbook.yml --extra-vars "@extra-vars.json"',
                            cwd='.',
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            shell=True)

  while True:
    line = process.stdout.readline()
    if line == b'' and process.poll() != None:
        break
    sys.stdout.write(line.decode('utf-8'))
    sys.stdout.flush()

def write_as_json(content):
  filename = 'extra-vars.json'
  exists_file = os.path.isfile(filename)

  if exists_file:
      os.remove(filename)

  with open(filename, 'w') as file:
      file.write(json.dumps(content, indent=2))
      file.close()

def set_settings(arguments):
  return {
      'action': 'dump',
      'db': {
          'host': arguments.host,
          'port': arguments.port,
          'user': arguments.user,
          'password': arguments.password,
          'name': arguments.database
      }
  }

def main():
  parser = argparse.ArgumentParser(description='Backup mysql database')
  parser.add_argument('--host', required=True, help='Connect to host.')
  parser.add_argument('--user', required=True, help='User for login.')
  parser.add_argument('--password', required=True, help='Password to use when connecting to server.')
  parser.add_argument('--port', type=int, default=3306, help='Password to use when connecting to server.')
  parser.add_argument('--database', required=True, help='The name of the database to be dumped.')
  arguments = parser.parse_args()

  write_as_json(set_settings(arguments))
  execute()


if __name__ == '__main__':
    main()

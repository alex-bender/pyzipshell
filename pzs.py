#!/usr/bin/env python3
"""Zip file carver/explorer tool"""
import os
import cmd
import struct


class ZipFile():
    sig = 0x04034b50


class ZipShell(cmd.Cmd):
    intro = "Zip shell."
    prompt = "> "
    fd = None

    def do_open(self, arg):
        self.fd = open(arg)

    def do_read(self, arg):
        self.data = self.fd.read()

    def do_validate(self, arg):
        print(struct.unpack('i', self.data[:4])[0] == ZipFile().sig)

    def do_close(self, arg):
        self.fd.close()

    def do_quit(self, arg):
        os._exit(0)

    do_q = do_quit
    do_exit = do_quit

    def do_test(self, arg):
        self.onecmd('open example/example.zip')
        self.onecmd('read')
        self.onecmd('validate')
        self.onecmd('close')
        self.onecmd('exit')


def main():
    ZipShell().cmdloop()


if __name__ == "__main__":
    main()

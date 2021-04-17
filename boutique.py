#! /bin/env python3

import argh

import snap_handler
import apt_handler

if __name__ == '__main__':
    argh.dispatch_commands([snap_handler.snap, apt_handler.apt])

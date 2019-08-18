#!/usr/bin/env python3
# Jellyfin-seymour
# Copyright (C) 2019  Red_M ( http://bitbucket.com/Red_M )

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import sys
import json

class skinner(object):
    def __init__(self):
        self.config = self.load_config()
        f = open('template.css','r')
        self.template = f.read()
        f.close()
        self.skin()

    def debug_print(self, text):
        print(text)

    def load_config(self):
        f = open('config.json','r')
        conf = json.load(f)
        f.close()
        return(conf)

    def replace_into_template(self, theme_config):
        out = str(self.template)
        for key in theme_config:
            out = out.replace('###'+key+'###',theme_config[key])
        return(out)

    def skin(self):
        selected_theme = self.config['selected_theme']
        if selected_theme in self.config['themes']:
            theme_config = self.config['themes'][selected_theme]
            f = open('output.css','w')
            f.write(self.replace_into_template(theme_config))
            self.debug_print('Done!')
        else:
            self.debug_print('Bad theme selected.')

        if 'f' in locals():
            f.close()


def main():
    a = skinner()

if __name__=='__main__':
    main()

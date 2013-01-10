#!/usr/bin/env python

import os
import zipfile

class CBZ:
    def __init__(self, files):
        self.images = files

    def export(self, filename):
        z = zipfile.ZipFile(filename, 'w')
        try:
            for i, img in enumerate(self.images):
                z.write(img, arcname='Page %d.jpg' % i)
        finally:
            z.close()

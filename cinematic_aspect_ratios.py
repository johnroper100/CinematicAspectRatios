# Copyright 2017 John Roper
#
# ##### BEGIN GPL LICENSE BLOCK ######
#
# Cinematic Aspect Ratios (CAR) is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CAR is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CAR.  If not, see <http://www.gnu.org/licenses/>.
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Cinematic Aspect Ratios",
    "author": "John Roper",
    "version": (1, 0, 0),
    "blender": (2, 78, 0),
    "location": "Properties Editor > Render",
    "description": "Set the render resolution to a cinematic aspect ratio",
    "warning": "",
    "wiki_url": "http://jmroper.com/",
    "tracker_url": "mailto:johnroper100@gmail.com",
    "category": "Render"
}

import bpy
from bpy.props import EnumProperty

sizes = [("5k", "5k", ""),
         ("4k", "4k", ""),
         ("4kHD", "4kHD", ""),
         ("2k", "2k", ""),
         ("1080p", "1080p", ""),
         ("720p", "720p", "")]

ratios = [("1.33:1", "1.33:1", "4:3"),
          ("1.66:1", "1.66:1", "5:3"),
          ("1.77:1", "1.77:1", "16:9"),
          ("1.85:1", "1.85:1", ""),
          ("2:1", "2:1", ""),
          ("2.35:1", "2.35:1", ""),
          ("2.37:1", "2.37:1", "RED Wide"),
          ("2.39:1", "2.39:1", "Referred to as 2.40"),
          ("2.44", "2.44", "")]

size_values = {"5k_1.33:1": [5120, 3840],
               "5k_1.66:1": [5120, 3072],
               "5k_1.77:1": [5120, 2880],
               "5k_1.85:1": [5120, 2768],
               "5k_1.9:1": [5120, 2700],
               "5k_2:1": [5120, 2560],
               "5k_2.35:1": [5120, 2179],
               "5k_2.37:1": [5120, 2160],
               "5k_2.39:1": [5120, 2142],
               "5k_2.44": [5120, 2098],
               "4k_1.33:1": [4096, 3072],
               "4k_1.66:1": [4096, 2458],
               "4k_1.77:1": [4096, 2304],
               "4k_1.85:1": [4096, 2214],
               "4k_1.9:1": [4096, 2160],
               "4k_2:1": [4096, 2048],
               "4k_2.35:1": [4096, 1679],
               "4k_2.37:1": [4096, 1743],
               "4k_2.39:1": [4096, 1728],
               "4k_2.44": [4096, 1714],
               "4kHD_1.33:1": [3840, 2880],
               "4kHD_1.66:1": [3840, 2304],
               "4kHD_1.77:1": [3840, 2160],
               "4kHD_1.85:1": [3840, 2076],
               "4kHD_2:1": [3840, 1920],
               "4kHD_2.35:1": [3840, 1634],
               "4kHD_2.37:1": [3840, 1620],
               "4kHD_2.39:1": [3840, 1607],
               "4kHD_2.44": [3840, 1574],
               "2k_1.33:1": [2048, 1536],
               "2k_1.66:1": [2048, 1229],
               "2k_1.77:1": [2048, 1152],
               "2k_1.85:1": [2048, 1107],
               "2k_2:1": [2048, 1024],
               "2k_2.35:1": [2048, 871],
               "2k_2.37:1": [2048, 864],
               "2k_2.39:1": [2048, 858],
               "2k_2.44": [2048, 839],
               "1080p_1.33:1": [1920, 1440],
               "1080p_1.66:1": [1920, 1152],
               "1080p_1.77:1": [1920, 1080],
               "1080p_1.85:1": [1920, 1038],
               "1080p_2:1": [1920, 960],
               "1080p_2.35:1": [1920, 817],
               "1080p_2.37:1": [1920, 810],
               "1080p_2.39:1": [1920, 803],
               "1080p_2.44": [1920, 787],
               "720p_1.33:1": [1280, 962],
               "720p_1.66:1": [1280, 768],
               "720p_1.77:1": [1280, 720],
               "720p_1.85:1": [1280, 692],
               "720p_2:1": [1280, 640],
               "720p_2.35:1": [1280, 545],
               "720p_2.37:1": [1280, 540],
               "720p_2.39:1": [1280, 536],
               "720p_2.44": [1280, 525]}


def CAR_update_resolution(self, context):
    scene = bpy.context.scene
    res_item = scene.CAR_sizes+"_"+scene.CAR_ratios
    x_res = size_values[res_item][0]
    y_res = size_values[res_item][1]

    bpy.context.scene.render.resolution_x = x_res
    bpy.context.scene.render.resolution_y = y_res


def CAR_panel(self, context):
    layout = self.layout
    scene = bpy.context.scene

    row = layout.row()
    row.label("Cinematic Aspect Ratios:")

    row = layout.row()
    row.prop(scene, "CAR_sizes")

    row = layout.row()
    row.prop(scene, "CAR_ratios")


def register():
    bpy.types.Scene.CAR_sizes = EnumProperty(
        items=sizes,
        name="Image Size",
        description="The output image size",
        default="1080p",
        update=CAR_update_resolution)
    bpy.types.Scene.CAR_ratios = EnumProperty(
        items=ratios,
        name="Aspect Ratio",
        description="the output image ratio",
        default="1.77:1",
        update=CAR_update_resolution)
    bpy.types.RENDER_PT_dimensions.append(CAR_panel)


def unregister():
    bpy.types.RENDER_PT_dimensions.remove(CAR_panel)
    del bpy.types.Scene.CAR_sizes
    del bpy.types.Scene.CAR_ratios

if __name__ == "__main__":
    register()

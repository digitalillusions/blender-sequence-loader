bl_info = {
    "name": "Sim Loader",
    "description": "Loader for meshio supported mesh files/ simulation sequences",
    "author": "Hantao Hui",
    "version": (1, 0),
    "blender": (3, 1, 0),
    "warning": "",
    "support": "COMMUNITY",
    "category": "Import-Export",
}

import bpy
import os
import sys

current_folder = os.path.dirname(os.path.abspath(__file__))
if current_folder not in sys.path:
    sys.path.append(current_folder)

if bpy.context.preferences.filepaths.use_relative_paths == True:
    bpy.context.preferences.filepaths.use_relative_paths = False

from simloader import *

classes = [
    SIMLOADER_obj_property,
    SIMLOADER_scene_property,
    SIMLOADER_OT_load,
    SIMLOADER_OT_edit,
    SIMLOADER_OT_resetpt,
    SIMLOADER_OT_resetins,
    SIMLOADER_OT_resetmesh,
    SIMLOADER_Import,
    SIMLOADER_List_Panel,
    SIMLOADER_UL_Obj_List,
    SIMLOADER_Settings,
    SIMLOADER_Templates,
    SIMLOADER_UL_Att_List,
]


def register():
    bpy.app.handlers.load_post.append(SIMLOADER_initilize)
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TEXT_MT_templates.append(draw_template)
    bpy.types.Scene.SIMLOADER = bpy.props.PointerProperty(type=SIMLOADER_scene_property)
    bpy.types.Object.SIMLOADER = bpy.props.PointerProperty(type=SIMLOADER_obj_property)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.TEXT_MT_templates.remove(draw_template)
    del bpy.types.Scene.SIMLOADER
    del bpy.types.Object.SIMLOADER
    bpy.app.handlers.load_post.remove(SIMLOADER_initilize)
    unsubscribe_to_selected()


if __name__ == "__main__":

    # unregister()
    register()
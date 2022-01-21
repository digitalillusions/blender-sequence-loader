import bpy
from bpy.app.handlers import persistent
from .utils import show_message_box
import os

importer_list = []


def selected_callback():
    if not bpy.context.view_layer.objects.active:
        return
    name = bpy.context.active_object.name
    idx = bpy.data.collections['SIMLOADER'].objects.find(name)
    if idx >= 0:
        bpy.context.scene.SIMLOADER.selected_obj_num = idx


def subscribe_to_selected():
    # A known problem of this function,
    # This function will not be executed, when the first time this addon is installed.
    # It will start to work, e.g. restart the blender, then in `load_post` function, this function will be called and start to work
    import simloader
    bpy.msgbus.subscribe_rna(
        key=(bpy.types.LayerObjects, 'active'),
        #  don't know why it needs this owner, so I set owner to this module `meshioimporter`
        owner=simloader,
        #  no args
        args=(()),
        notify=selected_callback,
    )


def unsubscribe_to_selected():
    import simloader
    bpy.msgbus.clear_by_owner(simloader)

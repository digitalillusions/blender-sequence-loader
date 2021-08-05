importer = None
importer_list = []


from bpy.app.handlers import persistent
import bpy
import fileseq
from .particles_importer import *
from .mesh_importer import *
@persistent
def load_post(scene):
    global importer_list
    imported_list = bpy.context.scene.my_tool.imported
    for l in imported_list:
        if l.type==0:
            fs=fileseq.findSequenceOnDisk(l.pattern)
            Pi=particle_importer(fileseq =fs,mesh_name=l.mesh_name,emitter_obj_name=l.obj_name,sphere_obj_name=l.sphere_obj_name,material_name=l.material_name,tex_image_name=l.tex_image_name,radius=l.radius)
            for all_att in l.all_attributes:
                Pi.render_attributes.append(all_att.name)
            Pi.set_color_attribute(l.used_color_attribute.name)
            importer_list.append(Pi)
            bpy.app.handlers.frame_change_post.append(Pi)
        elif l.type == 1:
            fs=fileseq.findSequenceOnDisk(l.pattern)
            Mi=mesh_importer(fileseq =fs,mesh_name=l.mesh_name,obj_name=l.obj_name)
            importer_list.append(Mi)
            bpy.app.handlers.frame_change_post.append(Mi)

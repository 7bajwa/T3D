# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "TRE3D Tools",
    "author": "7Bajwa",
    "description": " Some Useful Pipeline tools",
    "blender": (4, 4, 0),
    "version": (0, 0, 2),
    "location": "View3D",
    "warning": "",
    "category": "Development",
}

import bpy, os, sys

from .t3d_panel import (
    T3D_PT_Tools,
    T3D_PT_Obj,
    # T3D_PT_Obj_Grab,
    T3D_PT_Mesh,
    T3D_PT_UVS
)

from .ops.t3d_ops_misc import (
    T3D_OT_MatVertGroup, 
    T3D_OT_MakeProj, 
    T3D_OT_CopyProject,
    T3D_OT_PurgeData, 
    T3D_OT_STreeFBX, 
    T3D_OT_PackedModel
)

from .ops.t3d_ops_obj import (
    T3D_OT_UnSubdiv
    # T3D_OT_Grabshot_ref,
    # T3D_OT_Grabshot
)

from .ops.t3d_ops_mesh import (
    T3D_OT_UnLoop
)

PROPS_Obj = [
    ('snap_folder', bpy.props.StringProperty(name="Snap Folder", subtype="DIR_PATH", default="")),
    ('suffix', bpy.props.CollectionProperty(name="Snaps"))
]



# Making list of the classes and operators
reg_classes = [
    #Panels
    T3D_PT_Tools,
    T3D_PT_Obj,
    # T3D_PT_Obj_Grab,
    T3D_PT_Mesh,
    T3D_PT_UVS,

    # Misc Operators
    T3D_OT_MatVertGroup,
    T3D_OT_MakeProj,
    T3D_OT_CopyProject,
    T3D_OT_PurgeData,
    T3D_OT_STreeFBX,
    T3D_OT_PackedModel,

    # Object Operators
    T3D_OT_UnSubdiv,
    # T3D_OT_Grabshot_ref,
    # T3D_OT_Grabshot,

    # Mesh Operators
    T3D_OT_UnLoop,    
]




# Register all operators and panels
def register():

    user_path = bpy.utils.resource_path('USER')
    shot_path = os.path.join(user_path, "grabshots")
    print(shot_path)

    try:
        os.mkdir(shot_path)
        print("folder at", shot_path, "created!")
        bpy.ops.preferences.asset_library_add(name="Grabshots", path=shot_path)
    except:
        print("Folder already exists!!")
        pass 

    scene = bpy.types.Scene

    scene.t3d_prop_snaps = bpy.props.PointerProperty(type=bpy.types.Collection, name="Snaps")
    scene.t3d_snap_folder = bpy.props.StringProperty(name="Snap Folder", subtype="DIR_PATH", default=shot_path)

    for c in reg_classes:
        bpy.utils.register_class(c)
    


def unregister():
    scene = bpy.types.Scene

    del scene.t3d_prop_snaps
    del scene.t3d_snap_folder


    for c in reg_classes:
        bpy.utils.unregister_class(c)



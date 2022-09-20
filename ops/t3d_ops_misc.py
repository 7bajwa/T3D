import bpy, os, shutil, bpy_extras
from bpy.props import EnumProperty
from bpy.types import PointerProperty, Operator, Header, Menu, Panel, PropertyGroup






class T3D_UTILS_Props(bpy.types.PropertyGroup):
    project_folder: bpy.props.StringProperty(
        name="Project Folder", description="", subtype="FILE_PATH", default=""
    )


class T3D_OT_MatVertGroup(bpy.types.Operator):
    """It will do something with vertex"""

    bl_idname = "object.vert_group_operator"
    bl_label = "Material Vertex Group"

    def execute(self, context):
        obj = bpy.context.active_object
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action="DESELECT")
        bpy.context.object.active_material_index = 1
        bpy.ops.object.material_slot_select()
        vg = obj.vertex_groups.new(name="Leaf")
        bpy.ops.object.vertex_group_assign()
        bpy.ops.object.editmode_toggle()
        return {"FINISHED"}

def select_set_active(object):
     bpy.ops.object.select_all(action='DESELECT')
     object.select_set(True)      
     bpy.context.view_layer.objects.active = object

class T3D_OT_STreeFBX(bpy.types.Operator):
    "Import Speedtree FBX"
    bl_idname = "object.stree_fbx"
    bl_label = "Speedtree FBX"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        bpy.ops.import_scene.fbx(filepath=str(self.filepath))
        bpy.ops.object.scale_clear(clear_delta=False)
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

        mat = bpy.data.materials.new(name="Leaf")
        mat.diffuse_color = (0.130664, 0.8, 0.110211, 1)

        objs = bpy.context.selected_objects
        obj_name = objs[-1].name
        objs.pop(-1)
        # print(objs)

        bpy.ops.object.select_all(action='DESELECT')
        for obj in objs:
            obj.name = obj_name + "_" + obj.name
            
            obj.data.materials[0] = mat

            for me in bpy.data.meshes:
                uvs = [uv for uv in me.uv_layers
                        if not uv.active_render]
                while uvs:
                    me.uv_layers.remove(uvs.pop())

            obj.select_set(True) 
        
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
       
        select_set_active(bpy.data.objects[obj_name])
        
        bpy.ops.object.delete() 

        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class T3D_OT_PackedModel(bpy.types.Operator):
    "Import Model and texture from zip file"
    bl_idname = "object.packed_model"
    bl_label = "Packed Model"

    filepath: bpy.props.StringProperty(subtype="FILE_PATH")

    def execute(self, context):
        print ("Imported")
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}

class T3D_OT_MakeProj(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    """It will create the project folders"""

    bl_idname = "object.make_project_folder"
    bl_label = "Make Project Folders"

    filename_ext = ""

    structure_type: EnumProperty(
            name="Structure Type",
            items=(('Proj_a', "Proj_a", ""),
                   ('Proj_b', "Proj_b", ""),
                   ),
            default='Proj_a',
            )
  
    def execute(self, context):

        if self.structure_type == 'Proj_a':
            self.proj_a_structure()

        if self.structure_type == 'Proj_b':
            self.proj_b_structure()
    
        return {"FINISHED"}

    def proj_a_structure(self):
        os.mkdir(self.filepath)
        open(os.path.join(self.filepath, os.path.basename(self.filepath)+'_01.blend'), 'a').close()
        open(os.path.join(self.filepath, os.path.basename(self.filepath)+'_01.fbx'), 'a').close()

    def proj_b_structure(self):
        #Main Folder
        os.mkdir(self.filepath)
        open(os.path.join(self.filepath, os.path.basename(self.filepath)+'_01.fbx'), 'a').close()

        #Master folder in main folder
        master_path = os.path.join(self.filepath, 'Master')
        os.mkdir(master_path)

        #Speedtree folder in Master folder
        speedtree_path = os.path.join(self.filepath, 'ST')
        os.mkdir(speedtree_path)
        open(os.path.join(speedtree_path, os.path.basename(self.filepath)+'_01.spm'), 'a').close()
        open(os.path.join(speedtree_path, os.path.basename(self.filepath)+'_01.fbx'), 'a').close()

        #Blender folder in Master folder
        blend_path = os.path.join(master_path, 'BL')
        os.mkdir(blend_path)
        open(os.path.join(blend_path, os.path.basename(self.filepath)+'_01.blend'), 'a').close()

        #Photoshop folder in Master folder
        photoshop_path = os.path.join(master_path, 'PS')
        os.mkdir(photoshop_path)
        open(os.path.join(photoshop_path, os.path.basename(self.filepath)+'_01.psd'), 'a').close()

        #Textures folder in Main folder
        textures_path = os.path.join(self.filepath, 'Textures')
        os.mkdir(textures_path)
        open(os.path.join(textures_path, os.path.basename(self.filepath)+'_01_BC.tga'), 'a').close()
        open(os.path.join(textures_path, os.path.basename(self.filepath)+'_01_NM.tga'), 'a').close()
        open(os.path.join(textures_path, os.path.basename(self.filepath)+'_01_SM.tga'), 'a').close()
        return {"FINISHED"}
        

class T3D_OT_CopyProject(bpy.types.Operator):
    """It will create the project folders"""

    bl_idname = "object.copy_project"
    bl_label = "Copy  Project"

    source_name: bpy.props.StringProperty(default='Asset_a1')
    new_name: bpy.props.StringProperty(default='Asset_b1')

    def_folder:bpy.props.StringProperty(name="Folder", subtype="DIR_PATH")

    def execute(self, context):

        # Source path 
        src = os.path.join(self.def_folder, str(self.source_name))
        # Destination path 
        dest = os.path.join(self.def_folder, str(self.new_name))
        self.copy_folder(src, dest)
        self.rename(dest, self.source_name, self.new_name)

        return {"FINISHED"}

    def copy_folder(self, src, dest):        
        # Copy the content of source to destination 
        if os.path.exists(dest):
            print('path exists!')
            return {"FINISHED"}
        shutil.copytree(src, dest)
        return {"FINISHED"}

    def rename(self, path, old, new):
        # rename files
        for root, _, filenames in os.walk(path):
            for filename in filenames:
                file = os.path.join(root, filename)
                os.rename(file, file.replace(old, new))
        # rename directories
        folder = (d for d in  os.listdir(path))
        for _, fn in enumerate(folder, 1):
            p1 = os.path.join(path, fn)
            if os.path.isdir(p1):
                os.rename(p1, p1.replace(old, new))

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def draw(self, context):
        row = self.layout
        row.prop(self, "def_folder", text="Location")
        row.prop(self, "source_name", text="Asset Old")
        row.prop(self, "new_name", text="New Name")
    



class T3D_OT_PurgeData(bpy.types.Operator):
    """It will clear the orphan data"""

    bl_idname = "object.purge_data"
    bl_label = "Purge Waste"

    def execute(self, context):
        for block in bpy.data.meshes:
            if block.users == 0:
                bpy.data.meshes.remove(block)

        for block in bpy.data.materials:
            if block.users == 0:
                bpy.data.materials.remove(block)

        for block in bpy.data.textures:
            if block.users == 0:
                bpy.data.textures.remove(block)

        for block in bpy.data.images:
            if block.users == 0:
                bpy.data.images.remove(block)
        print ("Purged")
        return {'FINISHED'}

class B3D_OT_MakeLODs(bpy.types.Operator):
    """It will make & Open LOD settings""" 
    bl_idname = "object.b3d_make_lods"
    bl_label = "Make LODs"

    def execute(self, context):
        #Select a model

        #Make a copy
        #Add _LOD1 Suffix
        #Assign Decimate at .6 poly reduction

        #Make a copy
        #Rename _LOD2 Suffix
        #Set the reduction value to .3

        print ("LODs")
        return {'FINISHED'}



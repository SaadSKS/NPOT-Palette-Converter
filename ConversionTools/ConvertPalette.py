import bpy
import bmesh


def main(context):
    obj = context.active_object
    me = obj.data
    bm = bmesh.from_edit_mesh(me)

    uv_layer = bm.loops.layers.uv.verify()

    # adjust uv coordinates
    

    
    #UV Remapping begins
    bpy.context.area.ui_type = 'UV'
    bpy.ops.uv.select_all(action='SELECT')
    bpy.ops.transform.translate(value=(7.47070312, -0, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.transform.translate(value=(-0, -0.46875, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    for x in range(15):
        bpy.ops.uv.select_all(action='SELECT')
        for face in bm.faces:
            for loop in face.loops:
                loop_uv = loop[uv_layer]
                # use xy position of the vertex as a uv coordinate
                if 0 <= loop_uv.uv.x <= 1 and 0 <= loop_uv.uv.y <= 1:
                    loop_uv.select = False
        bpy.ops.transform.translate(value=(0, 0.0625, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.translate(value=(-1, -0, -0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.uv.select_all(action='DESELECT')

    bmesh.update_edit_mesh(me)


class ConvertPalette(bpy.types.Operator):
    """UV Operator description"""
    bl_idname = "uv.simple_operator"
    bl_label = "Simple UV Operator"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj and obj.type == 'MESH' and obj.mode == 'EDIT'

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def register():
    bpy.utils.register_class(ConvertPalette)


def unregister():
    bpy.utils.unregister_class(ConvertPalette)


if __name__ == "__main__":
    register()


    #Fixed Scaling via Reference Cube
    bpy.context.area.ui_type = 'VIEW_3D'
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.editmode_toggle()
    bpy.context.area.ui_type = 'UV'
    bpy.ops.uv.select_all(action='SELECT')
    bpy.ops.transform.resize(value=(16, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.context.area.ui_type = 'VIEW_3D'
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects["PaletteMapper"].select_set(True)
    bpy.ops.object.hide_view_set(unselected=False)
    
    
    bpy.context.area.ui_type = 'VIEW_3D'
    bpy.ops.object.select_all(action='SELECT')
    bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
    bpy.ops.object.editmode_toggle()

    
    #UV Remapping Function
    bpy.ops.uv.simple_operator()
    
    #Bring back to object view
    bpy.context.area.ui_type = 'VIEW_3D'
    bpy.ops.object.editmode_toggle()
    bpy.context.space_data.shading.type = 'MATERIAL'


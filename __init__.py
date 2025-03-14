# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name": "SJ Set Bone Nator",
    "author": "CaptainHansode",
    "version": (1, 1, 0),
    "blender": (2, 80, 0),
    "location":  "View3D > Sidebar > Item Tab",
    "description": "Set the properties of the selected bone.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Rigging",
}


import bpy
import math
import mathutils
from bpy.app.handlers import persistent


@persistent
def sj_set_bone_sel_amt_changes(scene):
    r"""selection changeのイベントハンドラ"""
    obj = bpy.context.active_object
    if obj.type == "ARMATURE":
        print(obj)
    return True


def set_bone_group(self, context):
    r"""set bone group"""
    if self.b_grp == "":
        grp = None
    else:
        grp = context.active_object.pose.bone_groups[self.b_grp]
    for pbn in context.selected_pose_bones:
        pbn.bone_group = grp


def set_bone_parent(self, context):
    r"""set bone parent"""
    if self.bone_p == "":
        _bone_p = None
    else:
        _bone_p = context.active_object.data.edit_bones[self.bone_p]
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.parent = _bone_p


def set_bone_head(self, context):
    r"""bone tm"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.head = (self.head_x, self.head_y, self.head_z)


def set_bone_tail(self, context):
    r"""bone tm"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.tail = (self.tail_x, self.tail_y, self.tail_z)


def set_bone_roll(self, context):
    r"""bone tm"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.roll = math.radians(self.roll)


def set_bone_length(self, context):
    r"""bone tm"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.length = self.length

def set_bone_lock(self, context):
    r"""bone tm"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.lock = self.is_lock


def set_bone_use_connect(self, context):
    r"""set bone rot mode"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.use_connect = self.use_connect


def set_bone_use_local_location(self, context):
    r"""set bone rot mode"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.use_local_location = self.use_local_location


def set_bone_use_inherit_rotation(self, context):
    r"""set bone rot mode"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.use_inherit_rotation = self.use_inherit_rotation


def set_bone_inherit_scale(self, context):
    r"""set bone rot mode"""
    for bn in context.active_object.data.edit_bones:
        if bn.select is True:
            bn.inherit_scale = self.b_inherit_scale


# def set_hide(self, context):
#     r"""set bone hide"""
#     for pbn in context.selected_pose_bones:
#         context.object.data.bones[pbn.name].hide = self.is_hide


def set_cs(self, context):
    """set bone custom shape"""
    for pbn in context.selected_pose_bones:
        pbn.custom_shape = self.cs_obj


def set_cs_scale(self, context):
    r"""set bone cs scale"""
    for pbn in context.selected_pose_bones:
        if "custom_shape_scale" in dir(pbn):
            pbn.custom_shape_scale = self.cs_scale

def set_cs_scale_x(self, context):
    """set bone cs scale"""
    for pbn in context.selected_pose_bones:
        if "custom_shape_scale_xyz" in dir(pbn):
            _scl = pbn.custom_shape_scale_xyz
            pbn.custom_shape_scale_xyz = mathutils.Vector((self.cs_scale_x, _scl[1], _scl[2]))

def set_cs_scale_y(self, context):
    """set bone cs scale"""
    for pbn in context.selected_pose_bones:
        if "custom_shape_scale_xyz" in dir(pbn):
            _scl = pbn.custom_shape_scale_xyz
            pbn.custom_shape_scale_xyz = mathutils.Vector((_scl[0], self.cs_scale_y, _scl[2]))

def set_cs_scale_z(self, context):
    """set bone cs scale"""
    for pbn in context.selected_pose_bones:
        if "custom_shape_scale_xyz" in dir(pbn):
            _scl = pbn.custom_shape_scale_xyz
            pbn.custom_shape_scale_xyz = mathutils.Vector((_scl[0], _scl[1], self.cs_scale_z))

def set_bone_size(self, context):
    r"""set bone cs b length"""
    for pbn in context.selected_pose_bones:
        pbn.use_custom_shape_bone_size = self.use_scl_b_size


def set_show_wire(self, context):
    r"""set bone show wire"""
    for pbn in context.selected_pose_bones:
        # pbn.show_wire = self.show_wire
        context.object.data.bones[pbn.name].show_wire = self.show_wire


def set_bone_rotation_mode(self, context):
    r"""set bone rot mode"""
    for pbn in context.selected_pose_bones:
        context.active_object.pose.bones[pbn.name].rotation_mode = self.b_rot_mode


class SJRenameBone(bpy.types.Operator):
    r"""Ser Bone Name"""
    bl_idname = "sj_set_bone.rename_bone"
    bl_label = "Rename"
    bl_description = "Rename selected bone name."

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        sjsb = context.scene.sj_set_bone_nator_props
        cnt = sjsb.s_num

        for pbn in bpy.context.selected_pose_bones:
            new_name = sjsb.b_name
            cnt_str = str(cnt)
            if sjsb.numbering is True:
                while len(cnt_str) < sjsb.n_digit:  # 0 fill
                    cnt_str = "0{}".format(cnt_str)
                pbn.name = "{}{}".format(new_name, cnt_str)
            else:
                pbn.name = new_name
            cnt += 1

        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  # 再描画
        return {'FINISHED'}


class SJSelBoneTree(bpy.types.Operator):
    r""""""
    bl_idname = "sj_set_bone.sel_bone_tree"
    bl_label = "Select Bone Tree"
    bl_description = "Select Bone Tree."

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def _get_children(self, c_objs):
        r"""ツリーを再帰回収"""
        ret = []
        for obj in c_objs:
            ret.append(obj.name)
            if len(obj.children) != 0:
                # 再帰
                ret.extend(self._get_children(obj.children))
        return ret

    def execute(self, context):
        r""""""
        
        # ポーズモードと編集モード2種類用意する
        if len(bpy.context.selected_pose_bones) == 0:
            return {'FINISHED'}
        
        sel_list = []
        
        for root_b in context.selected_pose_bones:
            sel_list.append(root_b.name)

            if len(root_b.children) != 0:
                sel_list.extend(self._get_children(root_b.children))

        bpy.ops.pose.select_all(action='DESELECT')  # 選択解除

        for b_name in sel_list:  # 選択
            context.active_object.pose.bones[b_name].bone.select = True

        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  # 再描画
        return {'FINISHED'}


class SJSelBoneRotationMode(bpy.types.Operator):
    r""""""
    bl_idname = "object.sj_sel_bone_rot_mode"
    bl_label = "Set Bone Rotation Mode"
    bl_description = "Set Rotation Mode."

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        for pbn in context.selected_pose_bones:  # 選択
            context.active_object.pose.bones[pbn.name].rotation_mode = 'XYZ'

        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  # 再描画
        return {'FINISHED'}


class SJResetBoneCustomShapes(bpy.types.Operator):
    r"""Ser Bone Name"""
    bl_idname = "sj_set_bone.reset_custom_shapes"
    bl_label = "Reset Bone Custom Shapes"
    bl_description = "Reset bone custom shape and group."

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        for pbn in context.selected_pose_bones:
            pbn.custom_shape = None
            pbn.use_custom_shape_bone_size = False
            if "bone_group" in pbn:
                pbn.bone_group = None  # 4.0で廃止
            if "custom_shape_scale" in pbn:
                pbn.custom_shape_scale = 1.0
            if "custom_shape_scale_xyz" in pbn:
                vec = mathutils.Vector((1.0, 1.0, 1.0))
                pbn.custom_shape_scale = vec
            context.object.data.bones[pbn.name].show_wire = False

        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  # 再描画
        return {'FINISHED'}


class SJCopyBoneTm(bpy.types.Operator):
    r""""""
    bl_idname = "sj_set_bone.copy_bn_tm"
    bl_label = "Copy Bone Transform"
    bl_description = "Copy Bone Transform."

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        sjsb = context.scene.sj_set_bone_nator_props
        amt = context.active_object
        for b in amt.data.edit_bones:
            if b.select is True:
                sjsb.head_x = b.head[0]
                sjsb.head_y = b.head[1]
                sjsb.head_z = b.head[2]
                sjsb.tail_x = b.tail[0]
                sjsb.tail_y = b.tail[1]
                sjsb.tail_z = b.tail[2]
                sjsb.roll = math.degrees(b.roll)
                sjsb.length = b.length
                break

        return {'FINISHED'}


class SJPasteBoneTm(bpy.types.Operator):
    r""""""
    bl_idname = "sj_set_bone.paste_bn_tm"
    bl_label = "Paste Bone Transform"
    bl_description = "Paste Bone Transform."

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def execute(self, context):
        r""""""
        sjsb = context.scene.sj_set_bone_nator_props
        amt = context.active_object
        for b in amt.data.edit_bones:
            if b.select is True:
                b.head = (sjsb.head_x, sjsb.head_y, sjsb.head_z)
                b.tail = (sjsb.tail_x, sjsb.tail_y, sjsb.tail_z)
                b.roll = math.radians(sjsb.roll)
                b.length = sjsb.length

        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  # 再描画
        return {'FINISHED'}


class SJSetBoneNatorProperties(bpy.types.PropertyGroup):
    r"""カスタムプロパティを定義する"""
    # name
    b_name: bpy.props.StringProperty(name="Name", default="")
    numbering: bpy.props.BoolProperty(
        name="Numbering", description="Numbering CheckBox", default=False)
    s_num: bpy.props.IntProperty(name="Start Number", default=0)
    n_digit: bpy.props.IntProperty(
        name="Digit", min=1, max=8, default=3)

    b_grp: bpy.props.StringProperty(name="Bone Group", update=set_bone_group)

    # is_hide: bpy.props.BoolProperty(name="Hide", default=False, update=set_hide)
    # cs_obj: bpy.props.StringProperty(name="Custom Shape", update=set_cs)
    cs_obj: bpy.props.PointerProperty(name="Custom Shape", type=bpy.types.Object, update=set_cs)

    cs_scale: bpy.props.FloatProperty(
        name="Scale", 
        default=1.0, 
        min=0.0, max=1000.0, step=0.10, precision=3, update=set_cs_scale)
    
    cs_scale_x: bpy.props.FloatProperty(
        name="Scale X", 
        default=1.0, 
        min=0.0, max=1000.0, step=0.10, precision=3, update=set_cs_scale_x)
    
    cs_scale_y: bpy.props.FloatProperty(
        name="Scale Y", 
        default=1.0, 
        min=0.0, max=1000.0, step=0.10, precision=3, update=set_cs_scale_y)
    
    cs_scale_z: bpy.props.FloatProperty(
        name="Scale Z", 
        default=1.0, 
        min=0.0, max=1000.0, step=0.10, precision=3, update=set_cs_scale_z)

    use_scl_b_size: bpy.props.BoolProperty(
        name="Scale to Bone Length", default=False, update=set_bone_size)

    show_wire: bpy.props.BoolProperty(
        name="Wireframe", default=False, update=set_show_wire)

    b_rot_mode: bpy.props.EnumProperty(
        items=[
            ("QUATERNION", "Quaternion (WXYZ)", ""),
            ("XYZ", "XYZ Euler", ""),
            ("XZY", "XZY Euler", ""),
            ("YXZ", "YXZ Euler", ""),
            ("YZX", "YZX Euler", ""),
            ("ZXY", "ZXY Euler", ""),
            ("ZYX", "ZYX Euler", ""),
            ("AXIS_ANGLE", "Axis Angle", "")
        ],
        name="Mode",
        update=set_bone_rotation_mode
    )

    # edit mode
    bone_p: bpy.props.StringProperty(name="Parent", update=set_bone_parent)
    # bone_p: bpy.props.PointerProperty(name="Parent", type=bpy.types.PoseBone, update=set_bone_parent)

    head_x: bpy.props.FloatProperty(
        name="X", default=0.0, min=-10000.0, max=10000.0, step=0.1)
    head_y: bpy.props.FloatProperty(        
        name="Y", default=0.0, min=-10000.0, max=10000.0, step=0.1)
    head_z: bpy.props.FloatProperty(
        name="Z", default=0.0, min=-10000.0, max=10000.0, step=0.1)

    tail_x: bpy.props.FloatProperty(
        name="X", default=0.0, min=-10000.0, max=10000.0, step=0.1)
    tail_y: bpy.props.FloatProperty(        
        name="Y", default=0.0, min=-10000.0, max=10000.0, step=0.1)
    tail_z: bpy.props.FloatProperty(
        name="Z", default=0.0, min=-10000.0, max=10000.0, step=0.1)

    roll: bpy.props.FloatProperty(name="Roll") # , update=set_bone_roll
    length: bpy.props.FloatProperty(name="Length") # , update=set_bone_length

    is_lock: bpy.props.BoolProperty(
        name="Lock", default=False, update=set_bone_lock)

    use_connect: bpy.props.BoolProperty(
        name="Connected", default=False, update=set_bone_use_connect)
    use_local_location: bpy.props.BoolProperty(
        name="Local Location", default=True, update=set_bone_use_local_location)
    use_inherit_rotation: bpy.props.BoolProperty(
        name="Inherit Rotation", default=True, update=set_bone_use_inherit_rotation)
    b_inherit_scale: bpy.props.EnumProperty(
        items=[
            ("FULL", "Full", ""),
            ("FIX_SHEAR", "Fix Shear", ""),
            ("ALIGNED", "Aligned", ""),
            ("AVERAGE", "Average", ""),
            ("NONE", "None", ""),
            ("NONE_LEGACY", "None (Legacy)", "")
        ],
        name="Inherit Scale",
        update=set_bone_inherit_scale
    )


class SJSetBoneNatorEditBnPanel(bpy.types.Panel):
    r"""UI"""
    bl_label = "SJ Set Bone Nator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # UIのタイプ
    bl_context = "armature_edit"  # ポーズモード以外は使えない

    # カスタムタブは名前を指定するだけで問題ない 他のツールのタブにも追加できる
    bl_category = 'Tool'
    # bl_category = 'SJTools'
    bl_options = {'DEFAULT_CLOSED'}  # デフォルトでは閉じている

    def draw(self, context):
        layout = self.layout
        sjsb = context.scene.sj_set_bone_nator_props

        layout.label(text="Transform", icon='RADIOBUT_ON')
        col = layout.column(align=True)
        col.label(text="Head")
        col.prop(sjsb, "head_x")
        col.prop(sjsb, "head_y")
        col.prop(sjsb, "head_z")

        col = layout.column(align=True)
        col.label(text="Tail")
        col.prop(sjsb, "tail_x")
        col.prop(sjsb, "tail_y")
        col.prop(sjsb, "tail_z")

        col = layout.column(align=True)
        col.prop(sjsb, "roll")

        col = layout.column(align=True)
        col.prop(sjsb, "length")

        row = layout.row(align=True)
        row.scale_y = 1.5
        row.operator("sj_set_bone.copy_bn_tm")
        row.operator("sj_set_bone.paste_bn_tm")

        col = layout.column(align=True)
        col.prop(sjsb, "is_lock", text="Lock")
        layout.separator(factor=2)

        layout.label(text="Relationship", icon='RADIOBUT_ON')
        col = layout.column(align=True)
        col.prop_search(sjsb, "bone_p", context.active_object.data, "edit_bones")
        col.prop(sjsb, "use_connect", text="Connected")
        col.prop(sjsb, "use_local_location", text="Local Location")
        col.prop(sjsb, "use_inherit_rotation", text="Inherit Rotation")
        layout.prop(sjsb, "b_inherit_scale", text='Inherit Scale')
        # layout.prop(sjsb, "is_hide")


class SJSetBoneNatorPoseModePanel(bpy.types.Panel):
    r"""UI"""
    bl_label = "SJ Set Bone Nator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'  # UIのタイプ
    bl_context = "posemode"  # ポーズモード以外は使えない

    # カスタムタブは名前を指定するだけで問題ない 他のツールのタブにも追加できる
    bl_category = 'Tool'
    # bl_category = 'SJTools'
    bl_options = {'DEFAULT_CLOSED'}  # デフォルトでは閉じている

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        sjsb = context.scene.sj_set_bone_nator_props

        layout.label(text="Select Tree", icon='RADIOBUT_ON')
        row = layout.row()
        row.scale_y = 1.5
        row.operator("sj_set_bone.sel_bone_tree")

        layout.separator(factor=2)

        layout.label(text="Rename", icon='RADIOBUT_ON')
        row = layout.row()
        row.prop(sjsb, "b_name")
        row = layout.row()
        row.prop(sjsb, "numbering")
        row.prop(sjsb, "s_num")
        row.prop(sjsb, "n_digit")
        row = layout.row()
        row.scale_y = 1.5
        row.operator("sj_set_bone.rename_bone")

        layout.separator(factor=2)

        # 4.0でLayer廃止
        if bpy.app.version[0] < 4:
            layout.label(text="Set Bone Layer", icon='RADIOBUT_ON')
            row = layout.row(align=True)
            row.operator("sj_set_bone.set_ly0")
            row.operator("sj_set_bone.set_ly1")
            row.operator("sj_set_bone.set_ly2")
            row.operator("sj_set_bone.set_ly3")
            row.operator("sj_set_bone.set_ly4")
            row.operator("sj_set_bone.set_ly5")
            row.operator("sj_set_bone.set_ly6")
            row.operator("sj_set_bone.set_ly7")
            row.separator(factor=3)
            row.operator("sj_set_bone.set_ly8")
            row.operator("sj_set_bone.set_ly9")
            row.operator("sj_set_bone.set_ly10")
            row.operator("sj_set_bone.set_ly11")
            row.operator("sj_set_bone.set_ly12")
            row.operator("sj_set_bone.set_ly13")
            row.operator("sj_set_bone.set_ly14")
            row.operator("sj_set_bone.set_ly15")
            row = layout.row(align=True)
            row.operator("sj_set_bone.set_ly16")
            row.operator("sj_set_bone.set_ly17")
            row.operator("sj_set_bone.set_ly18")
            row.operator("sj_set_bone.set_ly19")
            row.operator("sj_set_bone.set_ly20")
            row.operator("sj_set_bone.set_ly21")
            row.operator("sj_set_bone.set_ly22")
            row.operator("sj_set_bone.set_ly23")
            row.separator(factor=3)
            row.operator("sj_set_bone.set_ly24")
            row.operator("sj_set_bone.set_ly25")
            row.operator("sj_set_bone.set_ly26")
            row.operator("sj_set_bone.set_ly27")
            row.operator("sj_set_bone.set_ly28")
            row.operator("sj_set_bone.set_ly29")
            row.operator("sj_set_bone.set_ly30")
            row.operator("sj_set_bone.set_ly31")

            row = layout.row()
            row.operator("sj_set_bone.clear_layer")

            layout.separator(factor=2)

            layout.label(text="Set Bone Group", icon='RADIOBUT_ON')  # 4.0以降で廃止
            col = layout.column()
            col.prop_search(sjsb, "b_grp", context.active_object.pose, "bone_groups")
            # layout.prop(sjsb, "is_hide")

        layout.separator(factor=2)

        layout.label(text="Set Bone Custom Shape", icon='RADIOBUT_ON')
        row = layout.row()
        row.prop_search(sjsb, "cs_obj", context.scene, "objects")
        
        if bpy.app.version[0] < 4:
            layout.prop(sjsb, "cs_scale")
        else:
            col = layout.column()
            col.prop(sjsb, "cs_scale_x")
            col.prop(sjsb, "cs_scale_y")
            col.prop(sjsb, "cs_scale_z")

        layout.prop(sjsb, "use_scl_b_size")
        layout.prop(sjsb, "show_wire")
        layout.operator("sj_set_bone.reset_custom_shapes")

        layout.separator(factor=2)

        layout.label(text="Set Bone Rotation Mode", icon='RADIOBUT_ON')
        layout.prop(sjsb, "b_rot_mode")


class SJSetBoneLy(object):
    r"""set lay"""
    def __init__(self, *args, **kwargs):
        if len(bpy.context.selected_pose_bones) == 0:
            return None
        b = bpy.context.selected_pose_bones[-0]
        ret = bpy.context.object.data.bones[b.name]
        print("-" * 80)
        print(dir(bpy.context.object.data))
        print(ret)
        print(dir(bpy.context.object.data.bones[b.name]))

        sw = bpy.context.object.data.bones[b.name].layers[args[0]]
        self.set_bone_layer(
            bpy.context.selected_pose_bones, [args[0]], not(sw))
        return None

    def set_bone_layer(self, pbn_list=[], ly_list=[0], sw=True):
        r"""set bone layers"""
        # 一旦レイヤー状態を保存
        saved_layers = [
            layer_bool for layer_bool in bpy.context.active_object.data.layers]
        # 表示
        for ly in range(0, 32):
            bpy.context.active_object.data.layers[ly] = True
        
        for pbn in pbn_list:
            for ly in ly_list:
                bpy.context.object.data.bones[pbn.name].layers[ly] = sw
        
        # 表示状態を復元して終わり
        for i, layer_bool in enumerate(saved_layers):
            bpy.context.active_object.data.layers[i] = layer_bool

        return True


class SJSetBoneLy0(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 0
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy1(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 1
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy2(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 2
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy3(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 3
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy4(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 4
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy5(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 5
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy6(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 6
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy7(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 7
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy8(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 8
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy9(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 9
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy10(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 10
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy11(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 11
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy12(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 12
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy13(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 13
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy14(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 14
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy15(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 15
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy16(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 16
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy17(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 17
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy18(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 18
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy19(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 19
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy20(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 20
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy21(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 21
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy22(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 22
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy23(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 23
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy24(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 24
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy25(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 25
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy26(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 26
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy27(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 27
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy28(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 28
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy29(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 29
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy30(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 30
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneLy31(bpy.types.Operator):
    r"""Ser Bone Layer"""
    ly = 31
    bl_idname = "sj_set_bone.set_ly{}".format(ly)
    bl_label = str(ly)

    def execute(self, context):
        sbl = SJSetBoneLy(self.ly)
        del sbl
        return {'FINISHED'}


class SJSetBoneClearLayer(bpy.types.Operator):
    r"""Ser Bone Clear Layer"""
    bl_idname = "sj_set_bone.clear_layer"
    bl_label = "Clear"
    bl_description = "Change the settings of the selected bone layer."

    @classmethod
    def poll(cls, context):
        r""""""
        return context.active_object is not None

    def clear_bone_layer(self, pbn_list=[], ly_list=[0], sw=True):
        r"""set bone layers"""
        # 一旦レイヤー状態を保存
        saved_layers = [
            layer_bool for layer_bool in bpy.context.active_object.data.layers]
        # 表示
        for ly in range(0, 32):
            bpy.context.active_object.data.layers[ly] = True
        
        for pbn in pbn_list:
            for ly in ly_list:
                bpy.context.object.data.bones[pbn.name].layers[ly] = sw
        
        # 表示状態を復元して終わり
        for i, layer_bool in enumerate(saved_layers):
            bpy.context.active_object.data.layers[i] = layer_bool

    def execute(self, context):
        r""""""
        b_layers = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
            16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        # bones_data = bpy.context.active_object.data.bones
        # 0を設定
        self.clear_bone_layer(bpy.context.selected_pose_bones, [0], True)
        # クリア
        self.clear_bone_layer(bpy.context.selected_pose_bones, b_layers, False)
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)  # 再描画
        return {'FINISHED'}


classes = (
    SJSetBoneNatorProperties, SJSelBoneTree, SJResetBoneCustomShapes,
    SJCopyBoneTm, SJPasteBoneTm,
    SJSetBoneNatorPoseModePanel,
    SJSetBoneNatorEditBnPanel,
    SJRenameBone, SJSelBoneRotationMode,
    SJSetBoneLy0, SJSetBoneLy1, SJSetBoneLy2, SJSetBoneLy3, SJSetBoneLy4,
    SJSetBoneLy5, SJSetBoneLy6, SJSetBoneLy7, SJSetBoneLy8, SJSetBoneLy9,
    SJSetBoneLy10, SJSetBoneLy11, SJSetBoneLy12, SJSetBoneLy13, SJSetBoneLy14,
    SJSetBoneLy15, SJSetBoneLy16, SJSetBoneLy17, SJSetBoneLy18, SJSetBoneLy19,
    SJSetBoneLy20, SJSetBoneLy21, SJSetBoneLy22, SJSetBoneLy23, SJSetBoneLy24,
    SJSetBoneLy25, SJSetBoneLy26, SJSetBoneLy27, SJSetBoneLy28, SJSetBoneLy29,
    SJSetBoneLy30, SJSetBoneLy31, SJSetBoneClearLayer
    # ToggledModalOperator
    )


# Register all operators and panels
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # プロパティを追加する
    bpy.types.Scene.sj_set_bone_nator_props = bpy.props.PointerProperty(
        type=SJSetBoneNatorProperties)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    # プロパティを削除
    del bpy.types.Scene.sj_set_bone_nator_props


if __name__ == "__main__":
    register()

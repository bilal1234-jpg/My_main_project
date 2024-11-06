# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path
import sys
import os
path =  os.path.abspath('.')

a = Analysis(
    ['main_pose_app.py'],
    pathex=[path],
    binaries=[],
    datas=[
        ('assets/images/*','assets/images'),
        ('assets/database/*','assets/database'),
        ('assets/models/*','assets/models'),
        ('assets/pre_train/multipose_lightning/**/*', 'assets/pre_train/multipose_lightning'),
        ('assets/pre_train/multipose_lightning', 'assets/pre_train/multipose_lightning'),  
        ('assets/pre_train/thunder', 'assets/pre_train/thunder'),
        ('assets/videos/*','assets/videos'),
        ('other_resources/*.json','other_resources'),
        ('other_resources/*.txt','other_resources'),
        ('src/pyrebase_init.py', 'src'),
        ('src/download_vid.py', 'src'),
        ('src/voice.py', 'src'),
        ('src/kv.py', 'src'),
        ('src/sql_app.py', 'src'),
        ('src/violent.py', 'src'),
        
    ],
    hiddenimports=['tensorflow','tensorflow-hub', 'kivymd', 'cv2','Pyrebase','src.icon_definitions','src.pyrebase_init','src.download_vid', 'src.voice', 'src.kv', 'src.sql_app','src.violent'],
    hookspath=[kivymd_hooks_path],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
    cipher=None,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main_pose_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='assets/images/logo2.png',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main_pose_app',
)

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['app.py'],
    pathex=['C:\\Users\\messa\\Desktop\\vtt_changer'],
    binaries=[
        ('C:\\Users\\messa\\miniconda3\\envs\\new_env3\\python311.dll', '.'),  # python311.dllを追加
        ('C:\\Users\\messa\\miniconda3\\envs\\new_env3\\Lib\\encodings', 'encodings'),  # encodingsディレクトリを追加
    ],
    datas=[
        ('C:\\Users\\messa\\miniconda3\\envs\\new_env3\\Lib\\site-packages\\gradio\\blocks_events.py', 'gradio/'),
        ('C:\\Users\\messa\\miniconda3\\envs\\new_env3\\Lib\\site-packages\\gradio_client\\types.json', 'gradio_client/'),
        ('C:\\Users\\messa\\miniconda3\\envs\\new_env3\\Lib\\site-packages\\gradio\\templates\\frontend\\*.*', 'gradio/templates/frontend'),
        ('C:\\Users\\messa\\miniconda3\\envs\\new_env3\\Lib\\site-packages\\gradio\\templates\\frontend\\static\\img\\*.*', 'gradio/templates/frontend/static/img'),
    ],
    hiddenimports=[
        'gradio.blocks_events',
        'gradio',
        'gradio_client',
        'gradio_client.client',
        'gradio_client.compatibility',
        'gradio_client.serializing',
        'encodings',
        '_frontend_code',
        '_simple_templates',
        'test_data',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
    module_collection_mode={
        'gradio': 'py',  # Collect gradio package as source .py files
    },
)
pyz = PYZ(a.pure, a.zipped_data,
    cipher=block_cipher,
)
exe = EXE(pyz, a.scripts,
    [],
    exclude_binaries=False,  # ここをFalseに設定
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app')

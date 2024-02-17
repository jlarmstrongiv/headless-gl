{
  'variables': {
    'platform': '<(OS)',
    'openssl_fips': '0',
  },
  'targets': [
    {
      'target_name': 'webgl',
      'defines': [
        'VERSION=1.0.0'
      ],
      'sources': [
        'src/native/bindings.cc'
      ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'dependencies': [
        'webgl_lib'
      ]
    },
    {
      'target_name': 'webgl_lib',
      'type': 'static_library',
      'defines': [
        'VERSION=1.0.0'
      ],
      'sources': [
        'src/native/webgl.cc',
        'src/native/procs.cc'
      ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")",
        '<(module_root_dir)/deps/include',
        "angle/include"
      ],
      'dependencies': [
        'angle/src/angle.gyp:libEGL',
        'angle/src/angle.gyp:libGLESv2'
      ]
    }
  ]
}

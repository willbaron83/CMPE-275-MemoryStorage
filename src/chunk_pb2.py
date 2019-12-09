# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chunk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chunk.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x63hunk.proto\"\x17\n\x05\x43hunk\x12\x0e\n\x06\x62uffer\x18\x01 \x01(\x0c\"\x1a\n\x07Request\x12\x0f\n\x07hash_id\x18\x01 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1d\n\x0cReply_double\x12\r\n\x05\x62ytes\x18\x01 \x01(\x01\"\x0f\n\rEmpty_request\"\x1f\n\x0cReply_string\x12\x0f\n\x07hash_id\x18\x01 \x01(\t2\xd1\x01\n\nFileServer\x12\x1c\n\x06upload\x12\x06.Chunk\x1a\x06.Reply\"\x00(\x01\x12 \n\x08\x64ownload\x12\x08.Request\x1a\x06.Chunk\"\x00\x30\x01\x12=\n\x1aget_available_memory_bytes\x12\x0e.Empty_request\x1a\r.Reply_double\"\x00\x12\x44\n\x1fget_stored_hashes_list_iterator\x12\x0e.Empty_request\x1a\r.Reply_string\"\x00\x30\x01\x62\x06proto3')
)




_CHUNK = _descriptor.Descriptor(
  name='Chunk',
  full_name='Chunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buffer', full_name='Chunk.buffer', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=38,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash_id', full_name='Request.hash_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=66,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='Reply.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=92,
)


_REPLY_DOUBLE = _descriptor.Descriptor(
  name='Reply_double',
  full_name='Reply_double',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='Reply_double.bytes', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=123,
)


_EMPTY_REQUEST = _descriptor.Descriptor(
  name='Empty_request',
  full_name='Empty_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=140,
)


_REPLY_STRING = _descriptor.Descriptor(
  name='Reply_string',
  full_name='Reply_string',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash_id', full_name='Reply_string.hash_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=173,
)

DESCRIPTOR.message_types_by_name['Chunk'] = _CHUNK
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
DESCRIPTOR.message_types_by_name['Reply_double'] = _REPLY_DOUBLE
DESCRIPTOR.message_types_by_name['Empty_request'] = _EMPTY_REQUEST
DESCRIPTOR.message_types_by_name['Reply_string'] = _REPLY_STRING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Chunk = _reflection.GeneratedProtocolMessageType('Chunk', (_message.Message,), {
  'DESCRIPTOR' : _CHUNK,
  '__module__' : 'chunk_pb2'
  # @@protoc_insertion_point(class_scope:Chunk)
  })
_sym_db.RegisterMessage(Chunk)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'chunk_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'chunk_pb2'
  # @@protoc_insertion_point(class_scope:Reply)
  })
_sym_db.RegisterMessage(Reply)

Reply_double = _reflection.GeneratedProtocolMessageType('Reply_double', (_message.Message,), {
  'DESCRIPTOR' : _REPLY_DOUBLE,
  '__module__' : 'chunk_pb2'
  # @@protoc_insertion_point(class_scope:Reply_double)
  })
_sym_db.RegisterMessage(Reply_double)

Empty_request = _reflection.GeneratedProtocolMessageType('Empty_request', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY_REQUEST,
  '__module__' : 'chunk_pb2'
  # @@protoc_insertion_point(class_scope:Empty_request)
  })
_sym_db.RegisterMessage(Empty_request)

Reply_string = _reflection.GeneratedProtocolMessageType('Reply_string', (_message.Message,), {
  'DESCRIPTOR' : _REPLY_STRING,
  '__module__' : 'chunk_pb2'
  # @@protoc_insertion_point(class_scope:Reply_string)
  })
_sym_db.RegisterMessage(Reply_string)



_FILESERVER = _descriptor.ServiceDescriptor(
  name='FileServer',
  full_name='FileServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=176,
  serialized_end=385,
  methods=[
  _descriptor.MethodDescriptor(
    name='upload',
    full_name='FileServer.upload',
    index=0,
    containing_service=None,
    input_type=_CHUNK,
    output_type=_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='download',
    full_name='FileServer.download',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_CHUNK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_available_memory_bytes',
    full_name='FileServer.get_available_memory_bytes',
    index=2,
    containing_service=None,
    input_type=_EMPTY_REQUEST,
    output_type=_REPLY_DOUBLE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_stored_hashes_list_iterator',
    full_name='FileServer.get_stored_hashes_list_iterator',
    index=3,
    containing_service=None,
    input_type=_EMPTY_REQUEST,
    output_type=_REPLY_STRING,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILESERVER)

DESCRIPTOR.services_by_name['FileServer'] = _FILESERVER

# @@protoc_insertion_point(module_scope)

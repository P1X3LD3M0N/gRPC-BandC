# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trpc.proto\"W\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x05\x12\r\n\x05\x63lock\x18\x04 \x01(\x05\x12\x0f\n\x07\x62\x61nk_id\x18\x05 \x01(\x05\"V\n\x05Reply\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\x0e\n\x06result\x18\x03 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\x04 \x01(\x05\x12\r\n\x05\x63lock\x18\x05 \x01(\x05\"\x13\n\x03Req\x12\x0c\n\x04stop\x18\x01 \x01(\x08\"\x16\n\x03Rep\x12\x0f\n\x07stopped\x18\x01 \x01(\x08\x32>\n\x03RPC\x12!\n\x0bMsgDelivery\x12\x08.Request\x1a\x06.Reply\"\x00\x12\x14\n\x04\x43\x61ll\x12\x04.Req\x1a\x04.Rep\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=13
  _globals['_REQUEST']._serialized_end=100
  _globals['_REPLY']._serialized_start=102
  _globals['_REPLY']._serialized_end=188
  _globals['_REQ']._serialized_start=190
  _globals['_REQ']._serialized_end=209
  _globals['_REP']._serialized_start=211
  _globals['_REP']._serialized_end=233
  _globals['_RPC']._serialized_start=235
  _globals['_RPC']._serialized_end=297
# @@protoc_insertion_point(module_scope)

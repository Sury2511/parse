# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events/events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x65vents/events.proto\x12\x06\x65vents\"\xe1\x01\n\nEncapEvent\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x1c.events.EncapEvent.EventType\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"\x95\x01\n\tEventType\x12\r\n\tUNDEFINED\x10\x00\x12\x10\n\x0cUSER_CREATED\x10\x01\x12\x10\n\x0cUSER_UPDATED\x10\x02\x12\x12\n\x0eUSER_ACTIVATED\x10\x03\x12\x13\n\x0f\x43ONTRACT_SIGNED\x10\x04\x12\x15\n\x11\x43ONTRACT_APPROVED\x10\x05\x12\x15\n\x11\x43ONTRACT_REJECTED\x10\x06\"s\n\tUserEvent\x12\x13\n\x0binvestor_id\x18\x01 \x01(\x03\x12\x0f\n\x07\x62\x61nk_id\x18\x02 \x01(\x03\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x10\n\x08\x66ullname\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\"q\n\rContractEvent\x12\x13\n\x0binvestor_id\x18\x01 \x01(\x03\x12\x10\n\x08\x66ullname\x18\x02 \x01(\t\x12\x1c\n\x14identification_front\x18\x03 \x01(\t\x12\x1b\n\x13identification_back\x18\x04 \x01(\tB>\n\x18vn.entrade.models.eventsZ\"gitlab.com/enCapital/models/eventsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'events.events_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030vn.entrade.models.eventsZ\"gitlab.com/enCapital/models/events'
  _globals['_ENCAPEVENT']._serialized_start=32
  _globals['_ENCAPEVENT']._serialized_end=257
  _globals['_ENCAPEVENT_EVENTTYPE']._serialized_start=108
  _globals['_ENCAPEVENT_EVENTTYPE']._serialized_end=257
  _globals['_USEREVENT']._serialized_start=259
  _globals['_USEREVENT']._serialized_end=374
  _globals['_CONTRACTEVENT']._serialized_start=376
  _globals['_CONTRACTEVENT']._serialized_end=489
# @@protoc_insertion_point(module_scope)

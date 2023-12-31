# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import rpc_pb2 as rpc__pb2


class RPCStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MsgDelivery = channel.unary_unary(
                '/RPC/MsgDelivery',
                request_serializer=rpc__pb2.Request.SerializeToString,
                response_deserializer=rpc__pb2.Reply.FromString,
                )
        self.Call = channel.unary_unary(
                '/RPC/Call',
                request_serializer=rpc__pb2.Req.SerializeToString,
                response_deserializer=rpc__pb2.Rep.FromString,
                )


class RPCServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MsgDelivery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MsgDelivery': grpc.unary_unary_rpc_method_handler(
                    servicer.MsgDelivery,
                    request_deserializer=rpc__pb2.Request.FromString,
                    response_serializer=rpc__pb2.Reply.SerializeToString,
            ),
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=rpc__pb2.Req.FromString,
                    response_serializer=rpc__pb2.Rep.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RPC(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MsgDelivery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPC/MsgDelivery',
            rpc__pb2.Request.SerializeToString,
            rpc__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RPC/Call',
            rpc__pb2.Req.SerializeToString,
            rpc__pb2.Rep.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protos import pipeline_framework_pb2 as protos_dot_pipeline__framework__pb2


class PocBaseApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.execute = channel.unary_unary(
        '/pipeline_framework.PocBaseApi/execute',
        request_serializer=protos_dot_pipeline__framework__pb2.TaskResponse.SerializeToString,
        response_deserializer=protos_dot_pipeline__framework__pb2.TaskResponse.FromString,
        )


class PocBaseApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def execute(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PocBaseApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'execute': grpc.unary_unary_rpc_method_handler(
          servicer.execute,
          request_deserializer=protos_dot_pipeline__framework__pb2.TaskResponse.FromString,
          response_serializer=protos_dot_pipeline__framework__pb2.TaskResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pipeline_framework.PocBaseApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
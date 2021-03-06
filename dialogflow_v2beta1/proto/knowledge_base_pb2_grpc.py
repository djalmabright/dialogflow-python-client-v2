# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from dialogflow_v2beta1.proto import knowledge_base_pb2 as google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class KnowledgeBasesStub(object):
  """Manages knowledge bases.

  Allows users to setup and maintain knowledge bases with their knowledge data.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListKnowledgeBases = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.KnowledgeBases/ListKnowledgeBases',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.ListKnowledgeBasesRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.ListKnowledgeBasesResponse.FromString,
        )
    self.GetKnowledgeBase = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.KnowledgeBases/GetKnowledgeBase',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.GetKnowledgeBaseRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.KnowledgeBase.FromString,
        )
    self.CreateKnowledgeBase = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.KnowledgeBases/CreateKnowledgeBase',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.CreateKnowledgeBaseRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.KnowledgeBase.FromString,
        )
    self.DeleteKnowledgeBase = channel.unary_unary(
        '/google.cloud.dialogflow.v2beta1.KnowledgeBases/DeleteKnowledgeBase',
        request_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.DeleteKnowledgeBaseRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class KnowledgeBasesServicer(object):
  """Manages knowledge bases.

  Allows users to setup and maintain knowledge bases with their knowledge data.
  """

  def ListKnowledgeBases(self, request, context):
    """Returns the list of all knowledge bases of the specified agent.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetKnowledgeBase(self, request, context):
    """Retrieves the specified knowledge base.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateKnowledgeBase(self, request, context):
    """Creates a knowledge base.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteKnowledgeBase(self, request, context):
    """Deletes the specified knowledge base.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_KnowledgeBasesServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListKnowledgeBases': grpc.unary_unary_rpc_method_handler(
          servicer.ListKnowledgeBases,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.ListKnowledgeBasesRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.ListKnowledgeBasesResponse.SerializeToString,
      ),
      'GetKnowledgeBase': grpc.unary_unary_rpc_method_handler(
          servicer.GetKnowledgeBase,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.GetKnowledgeBaseRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.KnowledgeBase.SerializeToString,
      ),
      'CreateKnowledgeBase': grpc.unary_unary_rpc_method_handler(
          servicer.CreateKnowledgeBase,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.CreateKnowledgeBaseRequest.FromString,
          response_serializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.KnowledgeBase.SerializeToString,
      ),
      'DeleteKnowledgeBase': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteKnowledgeBase,
          request_deserializer=google_dot_cloud_dot_dialogflow__v2beta1_dot_proto_dot_knowledge__base__pb2.DeleteKnowledgeBaseRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.cloud.dialogflow.v2beta1.KnowledgeBases', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

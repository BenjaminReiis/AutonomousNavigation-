import 'dart:convert';

import 'package:web_socket_channel/web_socket_channel.dart';

class WebSocketService {
  late final WebSocketChannel channel;

  void connect(String url) {
    channel = WebSocketChannel.connect(
      Uri.parse(url),
    );
  }

  Stream get stream => channel.stream;

  void send(Map<String, dynamic> data) {
    channel.sink.add(jsonEncode(data));
  }

  void disconnect() {
    channel.sink.close();
  }
}

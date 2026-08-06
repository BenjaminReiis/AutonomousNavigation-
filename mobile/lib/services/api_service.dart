import 'dart:convert';

import 'package:http/http.dart' as http;

class ApiService {
  // Altere para o IP do computador onde o backend está rodando.
  // Exemplo: http://192.168.1.100:8000
  static const String baseUrl = "http://192.168.0.100:8000";

  Future<Map<String, dynamic>> sendCommand(String command) async {
    final response = await http.post(
      Uri.parse("$baseUrl/control/command/$command"),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }

    throw Exception("Erro ao enviar comando");
  }

  Future<List<dynamic>> getRobots() async {
    final response = await http.get(
      Uri.parse("$baseUrl/robots"),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body)["robots"];
    }

    throw Exception("Erro ao obter robôs");
  }

  Future<Map<String, dynamic>> getTelemetry() async {
    final response = await http.get(
      Uri.parse("$baseUrl/telemetry"),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    }

    throw Exception("Erro na telemetria");
  }
}

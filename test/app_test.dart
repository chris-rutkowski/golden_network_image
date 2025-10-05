import 'dart:io';

import 'package:fake_http_client/fake_http_client.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:golden_network_image/my_app.dart';

void main() {
  testWidgets('app test', (widgetTester) async {
    HttpOverrides.global = MockHttpOverrides();

    await widgetTester.pumpWidget(MyApp());
    final finder = find.byType(MyApp);

    // Problem:
    // The first.png snapshot doesn't display the network image, but the second.png does.
    // Solution:
    // ???

    await widgetTester.pumpAndSettle(); // doesn't add any value
    await widgetTester.pump(Duration(seconds: 1)); // doesn't add any value
    await expectLater(finder, matchesGoldenFile('first.png'));

    await widgetTester.pumpAndSettle();
    await expectLater(finder, matchesGoldenFile('second.png'));
  });
}

final class MockHttpOverrides extends HttpOverrides {

  @override
  HttpClient createHttpClient(SecurityContext? context) {
    return FakeHttpClient((request, client) async {
      debugPrint('Received network request:');
      final body = File('test/assets/green_square.bmp').readAsBytesSync();

      debugPrint('Responding with network image: ${body.length} bytes');
      return FakeHttpResponse(
        statusCode: 200,
        headers: {HttpHeaders.contentTypeHeader: 'image/bmp'},
        body: body,
      );
    });
  }
}

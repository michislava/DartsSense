#include <WebServer.h>
#include <WiFi.h>
#include <esp32cam.h> // Include the ESPAsyncWebServer library

WebServer server(80);

const char* ssid = "VIVACOM_FiberNet_C34F2";
const char* password = "Krasi6910";

static auto res = esp32cam::Resolution::find(400, 300);
void serveJpg()
{
  auto frame = esp32cam::capture();
  if (frame == nullptr) {
    Serial.println("CAPTURE FAIL");
    server.send(503, "", "");
    return;
  }
  Serial.printf("CAPTURE OK %dx%d %db\n", frame->getWidth(), frame->getHeight(),
                static_cast<int>(frame->size()));
 
  server.setContentLength(frame->size());
  server.send(200, "image/jpeg");
  WiFiClient client = server.client();
  frame->writeTo(client);
}
 
void handleFrames()
{
  if (!esp32cam::Camera.changeResolution(res)) {
    Serial.println("Set to resolution failed.");
  }
  serveJpg();
}
 
 
void  setup(){
  Serial.begin(115200);
  Serial.println();
  {
    using namespace esp32cam;
    Config cfg;
    cfg.setPins(pins::AiThinker);
    cfg.setResolution(res);
    cfg.setBufferCount(2);
    cfg.setJpeg(80);
 
    bool ok = Camera.begin(cfg);
    Serial.println(ok ? "CAMERA OK" : "CAMERA FAIL");
  }
  WiFi.persistent(false);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  Serial.print("http://");
  Serial.println(WiFi.localIP());
  Serial.println("  /getFrames.jpg");
  server.on("/getFrames.jpg", handleFrames);
 
  server.begin();
}
 
void loop()
{
  server.handleClient();
}
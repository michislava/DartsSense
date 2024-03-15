import React, { useEffect } from "react";
import axios from "axios";
import useWebSocket, { ReadyState } from "react-use-websocket";

export const Home = () => {
  const WS_URL = "ws://127.0.0.1:80";
  const { sendJsonMessage, lastJsonMessage, readyState } = useWebSocket(
    WS_URL,
    {
      share: false,
      shouldReconnect: () => true,
    }
  );

  // Run when the connection state (readyState) changes
  useEffect(() => {
    console.log("Connection state changed");
    if (readyState === ReadyState.OPEN) {
      sendJsonMessage({
        event: "subscribe",
        data: {
          channel: "general-chatroom",
        },
      });
    }
  }, [readyState, sendJsonMessage]);

  // Run when a new WebSocket message is received (lastJsonMessage)
  useEffect(() => {
    console.log("Got a new message:", lastJsonMessage);
    // Check if the lastJsonMessage is valid and contains required fields
    if (
      lastJsonMessage &&
      typeof lastJsonMessage === "object" &&
      "player" in lastJsonMessage &&
      "zone" in lastJsonMessage
    ) {
      // Send the lastJsonMessage to the backend
      axios
        .post("http://backend:9000/esp-data", lastJsonMessage)
        .then(() => {
          console.log("Data received and saved successfully");
        })
        .catch((error) => {
          console.error("Error sending data to the backend:", error);
        });
    }
  }, [lastJsonMessage]);

  return (
    <div>
      <h1>Home Page</h1>
      {/* Render any other components or JSX here */}
    </div>
  );
};

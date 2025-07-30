import React, { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { SendHorizonal, Sparkles } from "lucide-react";
import { motion } from "framer-motion";
import axios from "axios";

export default function VibeChatbot() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!input.trim()) return;
    const userMessage = { type: "user", content: input };
    setMessages([...messages, userMessage]);
    setLoading(true);
    setInput("");

    try {
      const res = await axios.post("/api/chat", { query: input });
      const botMessage = { type: "bot", content: res.data.answer };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { type: "bot", content: "⚠️ Failed to get response. Try again." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-black text-white p-4">
      <div className="max-w-3xl mx-auto flex flex-col gap-4">
        <h1 className="text-3xl font-bold text-center text-violet-400">
          <Sparkles className="inline mr-2 animate-pulse" /> Hercules Secure Chat
        </h1>

        <div className="flex flex-col gap-2 overflow-y-auto max-h-[70vh] p-2 border border-gray-700 rounded-xl bg-black/20 backdrop-blur shadow-lg">
          {messages.map((msg, idx) => (
            <motion.div
              key={idx}
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.3 }}
              className={`whitespace-pre-wrap text-sm px-4 py-2 rounded-xl max-w-[85%] ${
                msg.type === "user"
                  ? "ml-auto bg-violet-600 text-white"
                  : "mr-auto bg-gray-700"
              }`}
            >
              {msg.content}
            </motion.div>
          ))}
          {loading && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="text-gray-400 text-sm animate-pulse px-4 py-2"
            >
              Generating response...
            </motion.div>
          )}
        </div>

        <Card className="bg-gray-900 border border-gray-700 shadow-xl">
          <CardContent className="flex items-center p-2 gap-2">
            <Input
              className="bg-black text-white border-gray-600 focus-visible:ring-violet-400"
              placeholder="Ask about your code's security..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleSubmit()}
            />
            <Button onClick={handleSubmit} className="bg-violet-600 hover:bg-violet-500">
              <SendHorizonal className="h-4 w-4" />
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}

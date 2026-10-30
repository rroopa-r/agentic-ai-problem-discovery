"use client";
import { useState } from "react";

export default function DiscoveryDashboard() {
  const [topic, setTopic] = useState<string>("");
  const [result, setResult] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  const handleDiscovery = async () => {
    if (!topic) return;
    setLoading(true);
    setResult("");

    try {
      const response = await fetch("http://127.0.0.1:8000/discovery", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic: topic }), 
      });

      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }

      const data = await response.json();
      setResult(data.analysis || "No analysis returned");
    } catch (error: any) {
      console.error("Connection Error:", error);
      setResult("Error: Could not reach the backend. Check if the Python terminal is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 p-8">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-extrabold text-cyan-400 mb-4">
            Agentic Problem Discovery
          </h1>
          <p className="text-slate-400 text-lg">TinyLlama Research Assistant</p>
        </div>

        <div className="bg-slate-900 p-8 rounded-3xl border border-slate-800 mb-8">
          <input
            type="text"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            placeholder="Enter a topic..."
            className="w-full bg-slate-800 border border-slate-700 rounded-xl p-4 mb-4 outline-none focus:ring-2 focus:ring-cyan-500"
          />
          <button
            onClick={handleDiscovery}
            disabled={loading}
            className="w-full py-4 rounded-xl font-bold bg-cyan-600 hover:bg-cyan-500 disabled:bg-slate-700"
          >
            {loading ? "Agent is Researching..." : "Start Discovery Agent"}
          </button>
        </div>

        {result && (
          <div className="bg-slate-900 p-8 rounded-3xl border border-cyan-900/30">
            <h2 className="text-cyan-400 text-sm font-bold uppercase mb-4">Discovery Report</h2>
            <div className="text-slate-300 whitespace-pre-wrap">{result}</div>
          </div>
        )}
      </div>
    </main>
  );
}
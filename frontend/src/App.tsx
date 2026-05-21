import { useState } from "react";
import Panel from "./components/Panel";
import { api } from "./services/api";

const pretty = (data: unknown) => JSON.stringify(data, null, 2);

export default function App() {
  const [results, setResults] = useState<Record<string, string>>({});

  const run = async (key: string, fn: () => Promise<unknown>) => {
    setResults((r) => ({ ...r, [key]: "Running..." }));
    try {
      const out = await fn();
      setResults((r) => ({ ...r, [key]: pretty(out) }));
    } catch (err) {
      setResults((r) => ({ ...r, [key]: `Error: ${(err as Error).message}` }));
    }
  };

  return (
    <main>
      <header className="hero">
        <h1>AI for Low Pesticide Agriculture</h1>
        <p>Integrated vision, biology, robotics, and IoT to reduce pesticide usage by up to 90%.</p>
      </header>

      <section className="grid">
        <Panel
          title="Pest Detection"
          subtitle="Computer vision endpoint for crop pest identification"
          actionLabel="Run Detection"
          onRun={() => run("detect", api.detectPest)}
          result={results.detect || ""}
        />

        <Panel
          title="Biological Control"
          subtitle="Recommend beneficial organisms and bio-pesticides"
          actionLabel="Get Bio Plan"
          onRun={() => run("bio", api.bioControl)}
          result={results.bio || ""}
        />

        <Panel
          title="Precision Spray Planning"
          subtitle="Only spray high-risk patches to cut chemical use"
          actionLabel="Optimize Spray"
          onRun={() => run("spray", api.sprayPlan)}
          result={results.spray || ""}
        />

        <Panel
          title="Weather + Soil Fusion"
          subtitle="Merge sensor streams for intervention timing"
          actionLabel="Run Fusion"
          onRun={() => run("iot", api.iotFusion)}
          result={results.iot || ""}
        />

        <Panel
          title="Drone/Robot Path"
          subtitle="Grid path planning around blocked farm zones"
          actionLabel="Plan Route"
          onRun={() => run("robot", api.robotPath)}
          result={results.robot || ""}
        />

        <Panel
          title="Yield Prediction"
          subtitle="Estimate output impact from low-pesticide strategy"
          actionLabel="Forecast Yield"
          onRun={() => run("yield", api.yieldPrediction)}
          result={results.yield || ""}
        />
      </section>
    </main>
  );
}

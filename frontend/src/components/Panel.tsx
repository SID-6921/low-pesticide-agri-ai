import { ReactNode } from "react";

type PanelProps = {
  title: string;
  subtitle: string;
  actionLabel: string;
  onRun: () => void;
  result: string;
  children?: ReactNode;
};

export default function Panel({ title, subtitle, actionLabel, onRun, result, children }: PanelProps) {
  return (
    <section className="panel">
      <h3>{title}</h3>
      <p>{subtitle}</p>
      {children}
      <button onClick={onRun}>{actionLabel}</button>
      <pre>{result || "No result yet."}</pre>
    </section>
  );
}

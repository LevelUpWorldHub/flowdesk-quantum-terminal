async function getHealth() {
  try {
    const res = await fetch("http://127.0.0.1:8090/health", { cache: "no-store" });
    if (!res.ok) return null;
    return res.json();
  } catch {
    return null;
  }
}

export default async function Page() {
  const health = await getHealth();
  return (
    <main style={{ padding: 24 }}>
      <h1>FlowDesk Quantum Terminal</h1>
      <p style={{ opacity: 0.8 }}>Foundation shell — paper routing only.</p>
      <section style={{ marginTop: 24, display: "grid", gap: 12, gridTemplateColumns: "1fr 1fr 1fr" }}>
        <Pane title="Regime" body="GET /v1/regime/{symbol}" />
        <Pane title="IV Surface" body="GET /v1/iv-surface/{symbol}" />
        <Pane title="Paper Orders" body="POST /v1/paper/orders" />
      </section>
      <pre style={{ marginTop: 24, background: "#121a33", padding: 16, borderRadius: 8 }}>
        {JSON.stringify(health ?? { status: "api_offline" }, null, 2)}
      </pre>
    </main>
  );
}

function Pane({ title, body }: { title: string; body: string }) {
  return (
    <div style={{ background: "#121a33", border: "1px solid #243056", borderRadius: 8, padding: 16 }}>
      <strong>{title}</strong>
      <div style={{ opacity: 0.7, marginTop: 8, fontSize: 14 }}>{body}</div>
    </div>
  );
}

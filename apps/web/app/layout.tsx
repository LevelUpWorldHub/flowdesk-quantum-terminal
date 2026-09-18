import type { ReactNode } from "react";

export const metadata = {
  title: "FlowDesk Quantum Terminal",
  description: "Paper volatility terminal foundation",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, fontFamily: "ui-sans-serif, system-ui", background: "#0b1020", color: "#e8eefc" }}>
        {children}
      </body>
    </html>
  );
}

"use client";

import React from 'react';

interface CodeBlockProps {
  language: string;
  children: React.ReactNode;
  className?: string;
}

export default function CodeBlock({ language, children, className = '' }: CodeBlockProps) {
  return (
    <div className={`bg-slate-900 text-slate-100 p-4 rounded-xl overflow-x-auto font-mono text-sm ring-1 ring-white/10 ${className}`}>
      {children}
    </div>
  );
}

interface CodeLineProps {
  children: React.ReactNode;
  indent?: number;
  comment?: boolean;
  highlight?: boolean;
}

export function CodeLine({ children, indent = 0, comment = false, highlight = false }: CodeLineProps) {
  const indentSize = 2.0 * indent; // 2.0rem per indent level (double tabbed)
  const textColorClass = comment ? 'text-gray-500' : highlight ? 'text-yellow-400' : '';
  
  return (
    <div 
      className={`${textColorClass} whitespace-pre font-mono`}
      style={{ paddingLeft: `${indentSize}rem` }}
    >
      {children}
    </div>
  );
}

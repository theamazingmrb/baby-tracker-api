/**
 * This file provides TypeScript type declarations for Tailwind CSS classes
 * to prevent linting errors in CSS files that use Tailwind directives.
 */

declare module '*.css' {
  const content: { [className: string]: string };
  export default content;
}

// Declare the Tailwind CSS directives as valid
interface CSSRule {
  '@tailwind': string;
  '@apply': string;
  '@layer': string;
}

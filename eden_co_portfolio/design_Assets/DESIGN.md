---
name: Architectural Minimalist
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#c6c6cb'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#909095'
  outline-variant: '#45474b'
  surface-tint: '#c6c6cc'
  primary: '#c6c6cc'
  on-primary: '#2f3035'
  primary-container: '#0a0c10'
  on-primary-container: '#797a7f'
  inverse-primary: '#5d5e63'
  secondary: '#b8c3ff'
  on-secondary: '#002388'
  secondary-container: '#0043eb'
  on-secondary-container: '#c6ceff'
  tertiary: '#e9c176'
  on-tertiary: '#412d00'
  tertiary-container: '#130b00'
  on-tertiary-container: '#967533'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e8'
  primary-fixed-dim: '#c6c6cc'
  on-primary-fixed: '#1a1c20'
  on-primary-fixed-variant: '#45474b'
  secondary-fixed: '#dde1ff'
  secondary-fixed-dim: '#b8c3ff'
  on-secondary-fixed: '#001356'
  on-secondary-fixed-variant: '#0035be'
  tertiary-fixed: '#ffdea5'
  tertiary-fixed-dim: '#e9c176'
  on-tertiary-fixed: '#261900'
  on-tertiary-fixed-variant: '#5d4201'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
typography:
  display-lg:
    fontFamily: Bodoni Moda
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
  headline-md:
    fontFamily: Bodoni Moda
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Bodoni Moda
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 8px
  section-gap: 160px
  grid-gutter: 32px
  container-padding: 64px
---

## Brand & Style

The design system is built upon the intersection of structural permanence and digital fluidity. It serves a multi-disciplinary firm that operates at the highest level of craft, whether building physical interiors or complex software architectures. The brand personality is authoritative, precise, and intellectually rigorous.

The chosen style is **Architectural Minimalism**. This movement prioritizes structural integrity over decoration. It uses expansive whitespace as a functional element to provide "room to breathe" for high-stakes business strategy and complex data. The UI should evoke the feeling of a modern gallery or a high-end architectural studio: quiet, confident, and meticulously organized. Expect razor-sharp alignment, deliberate use of scale, and a "less but better" philosophy in every interaction.

## Colors

The palette is rooted in a "monolith" aesthetic. The foundation is built on **Deep Charcoal (#0A0C10)** and various shades of **Slate Gray**, creating a sophisticated, low-light environment that allows imagery and content to stand out.

**Electric Cobalt (#2E5BFF)** serves as the primary technical accent, used for interactive elements, progress indicators, and digital-first calls to action. **Burnished Gold (#C5A059)** is reserved for high-level editorial accents, heritage branding, or "Premium" service tiers, providing a warm, tactile contrast to the cool tech tones. Whites are kept "Crisp" (#F8F9FA) to ensure maximum legibility against the dark backgrounds.

## Typography

Typography follows a high-contrast logic to distinguish between "The Architect" (Serif) and "The Engineer" (Sans).

1.  **Headlines (Bodoni Moda):** A high-contrast serif that conveys luxury, history, and precision. Used for large display text and section titles.
2.  **Body (Hanken Grotesk):** A modern, highly legible sans-serif. It is utilitarian yet contemporary, ideal for explaining complex business strategies or software features.
3.  **Labels (JetBrains Mono):** A monospaced font used for metadata, categories, and technical specs. It reinforces the "Tech-Forward" aspect of the firm.

Large headings should use tight letter-spacing to feel "locked in," while labels should be generously tracked for an open, airy feel.

## Layout & Spacing

The layout philosophy is based on a **12-column Fixed Grid** with generous margins. Content is intentionally asymmetrical to mimic architectural blueprints. 

- **Whitespace as Content:** Margin and padding are not "empty space" but functional zones that direct the eye. Section gaps are intentionally large (160px+) to ensure each multidisciplinary service feels like its own distinct world.
- **Asymmetric Balance:** Align body text to a 6-column span while leaving the opposite 6 columns empty or filled with a single, high-impact image.
- **Breakpoints:** Mobile layouts shift to a single column, but maintain the high-contrast typography and generous vertical padding (80px) to preserve the premium feel.

## Elevation & Depth

This design system avoids heavy shadows, favoring **Tonal Layers** and **Glassmorphism** to create depth.

- **The Ground Plane:** The deepest charcoal (#0A0C10) is the base.
- **Elevated Surfaces:** Use subtle, semi-transparent overlays (Slate at 5-10% opacity) with a `20px` backdrop blur for modals and navigation bars. 
- **Outlines:** Use "Ghost Borders"—1px solid strokes in low-opacity slate (#FFFFFF at 10% opacity)—to define containers without adding visual weight.
- **Micro-interactions:** Elevation is communicated through motion rather than static shadows. When hovering over a card, the element should subtly scale (1.02x) or shift the border color to Electric Cobalt.

## Shapes

The shape language is **Sharp (0px)**. 

To mirror architectural precision and structural beams, there are no rounded corners in this design system. Buttons, cards, and input fields must be perfectly rectangular. This "hard edge" aesthetic reinforces the feeling of uncompromising quality and professional rigor. Decorative elements, if used, should be limited to thin horizontal or vertical lines (1px) that act as visual anchors for content.

## Components

### Buttons
- **Primary:** Sharp-edged, solid Electric Cobalt with white text. Hover state shifts to a slightly darker cobalt or adds a thin Gold border.
- **Ghost:** 1px white border, transparent background. Text in Hanken Grotesk (Medium).

### Cards & Project Grid
- Cards should have no borders by default. Use high-quality imagery that fills the container. 
- Project titles appear in Bodoni Moda on hover, using a glassmorphic overlay to ensure legibility.

### Input Fields
- Underline-only style or sharp-edged boxes with 1px slate borders. 
- Focus state triggers an Electric Cobalt underline and a subtle label shift.

### Lists
- Use JetBrains Mono for numbering (e.g., 01, 02, 03) to create a systematic, technical feel. 
- Large spacing between list items to allow for descriptive subtext.

### Hero Sections
- Full-bleed imagery or video backgrounds with a "Monolith" headline centered or bottom-aligned. 
- A subtle scroll-indicator (1px vertical line) should guide the user downward.
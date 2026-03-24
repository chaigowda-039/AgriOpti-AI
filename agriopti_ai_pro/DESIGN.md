# Design System Specification: The Precision Cultivator

## 1. Overview & Creative North Star
**Creative North Star: "The Earth’s Pulse"**
This design system moves away from the "industrial utility" aesthetic common in agriculture and moves toward a high-end, editorial-scientific experience. It treats data not as a spreadsheet, but as a living landscape. We achieve a "premium-bespoke" feel by balancing high-density data visualization with an expansive, atmospheric layout. 

The system rejects the rigid, boxy constraints of traditional dashboards. Instead, it utilizes **intentional asymmetry**, where large editorial headlines (`display-lg`) anchor the eye while dense data clusters breathe within vast, dark expanses. We prioritize depth through tonal layering and light-refraction (glassmorphism) over traditional flat containers, making the interface feel like a sophisticated lens through which the user monitors their land.

---

## 2. Colors
The palette is rooted in the "Nocturnal Earth" concept—a high-contrast dark mode that reduces eye strain during long monitoring sessions while making biological data "pop" with neon-naturalistic intensity.

### Palette Strategy
*   **Primary (Forest Green):** Used for growth, health, and primary positive actions. 
    *   *Token:* `primary` (#95d4b3) / `on_primary_container` (#76b394).
*   **Secondary (Terracotta/Soil):** Dedicated to soil health, harvest readiness, and substrate data.
    *   *Token:* `secondary` (#ffb77d) / `secondary_container` (#d97707).
*   **Tertiary (Atmospheric Blue):** Reserved for hydration levels, weather forecasts, and drone telemetry.
    *   *Token:* `tertiary` (#89ceff) / `tertiary_container` (#00405e).

### The "No-Line" Rule
To achieve a premium, seamless aesthetic, **1px solid borders are strictly prohibited** for sectioning. Structural boundaries must be defined through:
1.  **Background Color Shifts:** Placing a `surface_container_low` card on a `surface` background.
2.  **Tonal Transitions:** Using subtle shifts between `surface_container_lowest` and `surface_container_high` to distinguish content areas.

### The "Glass & Gradient" Rule
Flat buttons are for utility; signature actions are for performance. Main CTAs and high-level telemetry cards should utilize a subtle **Signature Texture**. For example, a primary action button should feature a linear gradient from `primary` to `primary_container` at a 135° angle, providing a "metallic-organic" luster. 

---

## 3. Typography
We employ a dual-type system to balance authoritative editorial style with extreme data density.

*   **Editorial Authority (Manrope):** Used for `display`, `headline`, and `title` scales. Manrope’s geometric yet warm character provides the "Director’s Voice"—it’s used to name sections or present high-level KPIs.
*   **Data Precision (Inter):** Used for `body` and `label` scales. Inter is optimized for the small-scale legibility required when displaying thousands of moisture-sensor coordinates or vehicle telemetry logs.

**Hierarchy as Identity:** 
High-contrast sizing is mandatory. A `display-lg` headline should often sit adjacent to a `label-sm` metadata point to create a sense of scale and precision.

---

## 4. Elevation & Depth
In this design system, depth is a narrative tool. We do not "box" items; we "layer" them.

### The Layering Principle
Depth is achieved by stacking `surface-container` tiers. 
*   **Base:** `surface` (#091421).
*   **Mid-Level Content:** `surface_container_low` (#121c2a).
*   **High-Priority Interactive Elements:** `surface_container_highest` (#2b3544).

### Ambient Shadows
Shadows must be invisible yet felt. When an element must "float" (e.g., a drone-control overlay), use a shadow with a blur value of `32px` or higher, with an opacity of `6%`. The shadow color must be a tinted version of the surface color (`#050f1c`), never a neutral black, to maintain the nocturnal atmosphere.

### The "Ghost Border" Fallback
Where accessibility requires a container boundary, use a **Ghost Border**: `outline_variant` (#414844) at `15%` opacity. It should act as a whisper of a line, not a wall.

---

## 5. Components

### Buttons
*   **Primary Action:** Roundedness `sm` (0.25rem). Gradient background (`primary` to `on_primary_container`). 
*   **Tertiary/Ghost:** No background. `label-md` typography in `on_surface_variant`. On hover, a subtle `surface_bright` background bleed-in.

### Cards & Telemetry Blocks
*   **Rule:** Forbid divider lines. 
*   **Implementation:** Use a `0.75rem` (md) vertical gap from the spacing scale to separate header text from data visualizations. Use `surface_container_low` as the card base to softly lift the content from the `surface` background.

### Inputs & Search
*   **Style:** Minimalist. Underline-only or subtle `surface_container_highest` fills. 
*   **Focus State:** Instead of a heavy border, use a `primary` (#95d4b3) glow—a 2px outer shadow with 20% opacity.

### Custom Agri-Tech Components
*   **Status Orbitals:** Instead of simple "Live" dots, use a pulse animation. A `primary` dot with a concentric, fading ring to indicate active data streaming.
*   **Soil Stratigraphy List:** A specialized list component using `secondary` (Terracotta) tonal shifts to represent different soil depths without using lines.

---

## 6. Do’s and Don’ts

### Do:
*   **Use Asymmetric Grids:** Align high-level stats to the left and granular lists to the right with different column widths (e.g., a 4-column vs 8-column split).
*   **Embrace Breathing Room:** Use the `16` (3.5rem) spacing token between major functional blocks to allow the "dark earth" background to frame the data.
*   **Layer Glassmorphism:** Use `backdrop-blur` on navigation sidebars to allow map data to subtly bleed through.

### Don't:
*   **Don't use 100% white text:** Use `on_surface` (#d9e3f6) for primary text to avoid "vibrating" against the dark background.
*   **Don't use hard borders:** Never use a solid 1px border to separate list items; use a `0.2rem` (1) vertical spacer instead.
*   **Don't crowd the viewport:** If a dashboard feels full, it’s broken. Move secondary data into a "Deep Dive" drawer using the `surface_container_high` token.
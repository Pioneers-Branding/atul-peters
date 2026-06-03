# Dr. Atul Peters - Homepage Revamp Specification

## 1. Concept & Vision

A premium, internationally-trusted healthcare website positioning Dr. Atul Peters as a leading bariatric and metabolic surgeon. The design conveys medical authority through clean sophistication, building instant trust while driving conversion toward consultations. The experience feels like walking into a world-class private hospital—calm, confident, and reassuring.

## 2. Design Language

### Aesthetic Direction
Premium healthcare meets modern SaaS—think Mayo Clinic's authority with Shopify's conversion craft. High whitespace, subtle gradients, and confident typography create an atmosphere of trust without clinical coldness.

### Color Palette
- **Primary**: `#1E3A5F` (Deep Navy - trust, authority)
- **Secondary**: `#2D8B6E` (Medical Teal - health, growth)
- **Accent**: `#E8B86D` (Warm Gold - premium, approachable)
- **Background**: `#FAFBFC` (Off-white - clean, spacious)
- **Surface**: `#FFFFFF` (Pure white for cards)
- **Text Primary**: `#1A1A2E` (Near black)
- **Text Secondary**: `#6B7280` (Muted gray)
- **Gradient**: `linear-gradient(135deg, #1E3A5F 0%, #2D8B6E 100%)`

### Typography
- **Headings**: Poppins (600, 700) - modern, confident, medical
- **Body**: Inter (400, 500) - highly readable, professional
- **Scale**:
  - H1: 3.5rem/4rem (hero)
  - H2: 2.5rem (section titles)
  - H3: 1.5rem (card titles)
  - Body: 1rem/1.125rem
  - Small: 0.875rem

### Spatial System
- Base unit: 8px
- Section padding: 80px/120px vertical
- Card padding: 32px
- Component gaps: 24px/32px
- Max content width: 1280px

### Motion Philosophy
- **Entrance**: Elements fade up (translateY: 20px → 0, opacity: 0 → 1) on scroll, 600ms ease-out, staggered 100ms
- **Hover**: Scale 1.02-1.05, shadow elevation, 200ms ease
- **Interactive**: Buttons press effect (scale 0.98), smooth color transitions
- **Counters**: Number animations counting up on viewport entry
- **Ambient**: Subtle gradient shifts on hero, floating elements

### Visual Assets
- **Icons**: Lucide Icons (consistent stroke, medical-appropriate)
- **Images**: High-quality medical imagery via Unsplash, professional headshots
- **Decorative**: Subtle dot patterns, soft gradient orbs, glassmorphism cards

## 3. Layout & Structure

### Page Flow
1. **Navigation** - Sticky, glass-effect, reveals on scroll up
2. **Hero** - Full viewport, video/image background with overlay, centered content
3. **Trust Strip** - Horizontal scrollable logos/achievements
4. **About Section** - Two-column asymmetric layout
5. **Specialties** - Icon card grid (3x3 → 2x2 → 1 column)
6. **Journey Timeline** - Horizontal stepper with connecting lines
7. **Transformations** - Before/after slider showcase
8. **Testimonials** - Video-first carousel
9. **International** - World map with flags
10. **Education Hub** - Featured article + grid layout
11. **FAQ** - Accordion with smooth expand
12. **CTA Banner** - Full-width gradient with appointment form
13. **Footer** - Multi-column dark footer

### Responsive Strategy
- **Desktop**: 1280px+ (full layouts)
- **Tablet**: 768px-1279px (adjusted grids, smaller type)
- **Mobile**: <768px (single column, hamburger nav, sticky CTAs)

## 4. Features & Interactions

### Navigation
- Logo left, links center, CTA right
- Hamburger menu on mobile with slide-in drawer
- Sticky behavior: hides on scroll down, shows on scroll up
- Active section highlighting

### Hero Section
- Background: gradient overlay on professional medical image
- **Carousel**: 5 banner slides with auto-rotation (6 seconds)
- Animated headline entrance (word by word)
- Floating particles/decorative elements
- Dual CTA buttons with hover glow
- Trust indicators animate in on load

### Treatment Cards
- Hover: lift + shadow + icon color change
- Click: smooth scroll to detail or modal
- Icon animation on hover

### Journey Timeline
- Horizontal scroll on desktop, vertical on mobile
- Active step highlighting
- Connecting line animation on scroll

### Before/After Slider
- Draggable slider divider
- Touch-enabled for mobile
- Smooth reveal animation

### FAQ Accordion
- Single open at a time (optional)
- Smooth height animation
- Rotate chevron indicator

### BMI Calculator
- Modal trigger
- Slider inputs for height/weight
- Real-time result display
- Color-coded BMI categories

### Floating CTAs
- WhatsApp button: fixed bottom-right
- Sticky appointment bar on mobile bottom

### Form Interactions
- Floating labels
- Real-time validation
- Success state animation
- Loading state on submit

## 5. Component Inventory

### Button
- **Primary**: Navy bg, white text, gold hover glow
- **Secondary**: White bg, navy border, navy text
- **Ghost**: Transparent, underline on hover
- **States**: Default, hover (lift + glow), active (press), disabled (50% opacity)

### Card
- White bg, 16px radius, subtle shadow
- Hover: translateY(-4px), increased shadow
- Optional: gradient border on hover

### Navigation Link
- Default: text-secondary
- Hover: text-primary with underline animation
- Active: text-primary, bold

### Input Field
- Floating label pattern
- Focus: border color change, label color change
- Error: red border, shake animation
- Valid: green checkmark

### Trust Badge
- Icon + number + label
- Counter animation on viewport entry
- Subtle pulse on load

### Accordion Item
- Header: question + chevron
- Content: answer text with padding
- Chevron rotates 180° when open

### Testimonial Card
- Video thumbnail with play button
- Patient name + procedure
- Star rating
- Quote preview

## 6. Technical Approach

### Architecture
- Single `index.html` with semantic sections
- `styles.css` with CSS custom properties for theming
- `main.js` with vanilla JS, no dependencies

### CSS Strategy
- CSS Grid + Flexbox for layouts
- CSS custom properties for colors/spacing
- `@media` queries for responsive
- `@keyframes` for animations
- `scroll-behavior: smooth` for anchor navigation

### JavaScript Features
- Intersection Observer for scroll animations
- Event delegation for accordion/cards
- requestAnimationFrame for counter animations
- Passive event listeners for performance

### Performance
- Lazy loading for below-fold images
- CSS containment for heavy sections
- Debounced scroll handlers
- Preconnect to font origins

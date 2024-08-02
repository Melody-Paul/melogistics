/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./core/templates/**/*.html"],
    theme: {
      extend: {},
    },
    plugins: [],
}

module.exports = {
  theme: {
    extend: {
      fontFamily: {
        'roboto': ['Roboto', 'sans-serif'],
      }
    }
  }
}

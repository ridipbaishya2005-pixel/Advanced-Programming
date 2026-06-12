import { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, SafeAreaView, StatusBar } from 'react-native';

export default function App() {
  const [count, setCount] = useState(0);
  const [isDarkMode, setIsDarkMode] = useState(false);

  const handleIncrement = () => setCount(prev => prev + 1);
  const handleDecrement = () => { if (count > 0) setCount(prev => prev - 1); };
  const handleReset = () => setCount(0);
  const toggleTheme = () => setIsDarkMode(prev => !prev);

  const theme = isDarkMode ? dark : light;

  return (
    <SafeAreaView style={[styles.safeArea, { backgroundColor: theme.bg }]}>
      <StatusBar
        barStyle={isDarkMode ? 'light-content' : 'dark-content'}
        backgroundColor={theme.bg}
      />

      <View style={[styles.container, { backgroundColor: theme.bg }]}>

        {/* Title */}
        <Text style={[styles.title, { color: theme.text }]}>Digital Counter</Text>

        {/* Counter display */}
        <View style={[styles.counterBox, { borderColor: theme.accent }]}>
          <Text style={[styles.counterText, { color: theme.accent }]}>{count}</Text>
          <Text style={[styles.counterLabel, { color: theme.subtext }]}>
            {count === 0 ? 'Start counting!' : count === 1 ? '1 tap so far' : `${count} taps so far`}
          </Text>
        </View>

        {/* Increment / Decrement row */}
        <View style={styles.row}>
          <TouchableOpacity
            style={[styles.btn, styles.btnLarge, { backgroundColor: theme.btnPrimary }]}
            onPress={handleDecrement}
            activeOpacity={count === 0 ? 1 : 0.75}
          >
            <Text style={[styles.btnText, { color: count === 0 ? theme.subtext : theme.btnText }]}>
              −
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.btn, styles.btnLarge, { backgroundColor: theme.btnPrimary }]}
            onPress={handleIncrement}
            activeOpacity={0.75}
          >
            <Text style={[styles.btnText, { color: theme.btnText }]}>+</Text>
          </TouchableOpacity>
        </View>

        {/* Reset button */}
        <TouchableOpacity
          style={[styles.btn, styles.btnWide, { backgroundColor: theme.btnSecondary }]}
          onPress={handleReset}
          activeOpacity={0.75}
        >
          <Text style={[styles.btnTextSmall, { color: theme.btnText }]}>Reset</Text>
        </TouchableOpacity>

        {/* Theme toggle */}
        <TouchableOpacity
          style={[styles.btn, styles.btnWide, styles.btnTheme, { borderColor: theme.accent }]}
          onPress={toggleTheme}
          activeOpacity={0.75}
        >
          <Text style={[styles.btnTextSmall, { color: theme.accent }]}>
            {isDarkMode ? '☀️  Light Mode' : '🌙  Dark Mode'}
          </Text>
        </TouchableOpacity>

      </View>
    </SafeAreaView>
  );
}

// ─── Themes ──────────────────────────────────────────────────────────────────

const light = {
  bg:          '#F5F5F5',
  text:        '#1A1A1A',
  subtext:     '#888888',
  accent:      '#4F46E5',
  btnPrimary:  '#4F46E5',
  btnSecondary:'#E0E0E0',
  btnText:     '#FFFFFF',
};

const dark = {
  bg:          '#121212',
  text:        '#F0F0F0',
  subtext:     '#777777',
  accent:      '#818CF8',
  btnPrimary:  '#3730A3',
  btnSecondary:'#2A2A2A',
  btnText:     '#F0F0F0',
};

// ─── Styles ───────────────────────────────────────────────────────────────────

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 32,
    gap: 16,
  },
  title: {
    fontSize: 22,
    fontWeight: '600',
    letterSpacing: 0.5,
    marginBottom: 8,
  },
  counterBox: {
    width: 200,
    height: 200,
    borderRadius: 100,
    borderWidth: 3,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 16,
  },
  counterText: {
    fontSize: 72,
    fontWeight: '700',
    lineHeight: 80,
  },
  counterLabel: {
    fontSize: 12,
    marginTop: 4,
  },
  row: {
    flexDirection: 'row',
    gap: 16,
  },
  btn: {
    borderRadius: 14,
    justifyContent: 'center',
    alignItems: 'center',
  },
  btnLarge: {
    width: 80,
    height: 80,
  },
  btnWide: {
    width: 176,
    height: 52,
  },
  btnTheme: {
    backgroundColor: 'transparent',
    borderWidth: 2,
  },
  btnText: {
    fontSize: 36,
    fontWeight: '300',
    lineHeight: 42,
  },
  btnTextSmall: {
    fontSize: 15,
    fontWeight: '600',
  },
});
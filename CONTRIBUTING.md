# Contributing to AgroGuard

Thank you for your interest in contributing to **AgroGuard**! We welcome contributions from researchers, agronomists, software developers, and machine learning practitioners.

---

## 🌿 How Can You Contribute?

1. **Reporting Bugs**: File detailed bug reports via GitHub Issues with steps to reproduce.
2. **Improving Model Architectures**: Experiment with higher-capacity backbones, data augmentations, or pruning/quantization.
3. **Agronomic Data & Advisory Expansion**: Refine phytosanitary advisories in `knowledge_base.py` with validated university or extension protocols.
4. **Web UI & Farmer Usability**: Enhance UI accessibility, offline caching, and mobile responsiveness.

---

## 🚀 Development Workflow

1. **Fork the Repository** and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/AgroGuard.git
   cd AgroGuard
   ```

2. **Create a Feature Branch**:
   ```bash
   git checkout -b feat/your-feature-name
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Locally**:
   Ensure the local diagnostic server launches without errors:
   ```bash
   python main.py
   ```

5. **Commit Your Changes**:
   Follow semantic commit message conventions:
   - `feat:` A new feature
   - `fix:` A bug fix
   - `docs:` Documentation updates
   - `refactor:` Code refactoring without behavior change

6. **Submit a Pull Request**:
   Push your branch to GitHub and open a Pull Request against the `main` branch with a clear description of your changes.

---

## 📜 Code of Conduct

Please review and respect our [Code of Conduct](CODE_OF_CONDUCT.md) in all community interactions.

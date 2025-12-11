# 🌀 2D Laminar Channel Flow Simulation using OpenFOAM

A beginner-friendly CFD project demonstrating laminar flow development in a 2D channel.
Mesh generated in Salome, solved with OpenFOAM (icoFoam), post-processed in ParaView.

---

### 📌 Objective
Simulate steady laminar flow and validate velocity & pressure behaviour
against theoretical Poiseuille solution.

---

### 🔧 Tools
- Salome (Meshing)
- OpenFOAM (icoFoam)
- ParaView (Post-processing)
- Python/Excel (Plotting)
- GitHub for documentation

---

### ⚙ Simulation Setup

| Parameter | Value |
|---|---|
| Length | 0.20 m |
| Height | 0.02 m |
| Fluid | Water |
| Velocity inlet | 0.01 m/s |
| Re ≈ | 200 (Laminar) |

---

### 📊 Results

| Plot | Description |
|---|---|
| ![vel](results/velocity_vs_length.png) | Velocity increases and stabilizes → fully developed flow |
| ![press](results/pressure_vs_length.png) | Pressure gradually decreases → viscous losses |
| ![ana](results/analytic_velocity_vs_height.png) | Analytical Parabolic velocity profile |

---

### 🧠 Key Learnings

- Converting mesh from Salome to OpenFOAM (`ideasUnvToFoam`)
- Setting BCs for 2D laminar flow
- Extracting centerline velocity
- Plotting velocity & pressure profiles
- Understanding developing vs fully developed flow

---

### 🚀 Future Work

- Add CFD velocity profile at outlet & compare with analytic curve
- Mesh refinement study
- Try turbulent models at higher Re (k-epsilon/k-omega)

---

### 📁 Project Structure

See folder tree in repository.

---

### ✉ Contact / Portfolio

Feel free to fork, run or extend.  
Good starting example for CFD learners.

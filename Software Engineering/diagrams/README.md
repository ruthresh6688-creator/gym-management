# Software Engineering Diagrams Catalog
## Scenario 27: Gym Membership Management and Fitness Activity Analysis System
**Institution:** Velalar College of Engineering and Technology, Erode - 12  
**Department:** Information Technology  
**Course:** 25ITT33 – Software Engineering (Unit 2 & Unit 3)  

---

### Index of Engineering Diagrams

| No. | Diagram Title | File Name | Syllabus Unit | Description |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **System Architecture Diagram** | [system_architecture_diagram.jpg](system_architecture_diagram.jpg) | Unit 3 | 3-Tier architecture showing Java Application, MySQL Database, Python Data Analysis Module, and Output Dashboards. |
| 2 | **Use Case Diagram** | [use_case_diagram.jpg](use_case_diagram.jpg) | Unit 2 | Actor interactions (Gym Administrator, Trainer, Member) and system use cases with `<<include>>` and `<<extend>>` relationships. |
| 3 | **Class Diagram** | [class_diagram.jpg](class_diagram.jpg) | Unit 2 & 3 | Static model showing classes (`Member`, `Membership`, `MembershipPlan`, `Trainer`, `TrainerAssignment`, `Attendance`, `ReportGenerator`, `AnalysisModule`), attributes, methods, and associations. |
| 4 | **Data Flow Diagram (DFD Level 0)** | [dfd_level_0.jpg](dfd_level_0.jpg) | Unit 2 | Context-level DFD demonstrating overall information exchange between external entities and the central Gym System. |
| 5 | **Data Flow Diagram (DFD Level 1)** | [dfd_level_1.jpg](dfd_level_1.jpg) | Unit 2 | Detailed functional decomposition showing processes 1.0 to 7.0 and data stores (D1 to D5). |
| 6 | **Sequence Diagram** | [sequence_diagram.jpg](sequence_diagram.jpg) | Unit 3 | Time-ordered chronological interaction for login, member management, registration, attendance, trainer assignment, and Python analysis. |
| 7 | **Activity Diagram** | [activity_diagram.jpg](activity_diagram.jpg) | Unit 3 | Operational control flow representing system login, branching menu options, attendance workflow, and analytics rendering. |
| 8 | **State Transition Diagram** | [state_transition_diagram.md](state_transition_diagram.md) | Unit 3 | Finite state machine capturing member lifecycle states (`Active`, `Expiring Soon`, `Expired`, `Renewed`) and attendance session states. |

> **Note on E-R Diagram:** As instructed by the syllabus guidelines, the Entity-Relationship (E-R) Diagram is maintained exclusively inside the `Database Management System/diagrams/` folder to adhere to DBMS course requirements.

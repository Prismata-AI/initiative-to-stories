# Stories - EPC-009

_2 stories._

---

## EPC-009-US-001 - Tool usable immediately from a browser without installing software

As a business analyst, I want to open the tool in my browser and start producing a process map without installing any software or plugin, so that I can evaluate and use the tool without any up-front setup cost.

**Acceptance criteria:**

**Scenario 1: Tool is fully functional in a standard browser with no prior installation**
Given I am using a current-version standard browser with no additional software, plugins, or extensions installed for this tool, when I navigate to the tool's address, then I can submit a process description and receive a rendered diagram without being prompted to install anything.

**Scenario 2: Tool does not require a specific browser or operating system**
Given I am using a different current-version standard browser than the one used in the primary test, when I navigate to the tool's address, then I can submit a process description and receive a rendered diagram without any browser-specific installation step.

**Scenario 3: Attempting to use the tool on an unsupported browser produces an informative message rather than a silent failure**
Given I am using a browser version that the tool does not support, when I navigate to the tool's address, then I receive a clear message explaining the limitation and identifying a supported alternative - rather than a broken or blank experience with no explanation.

**Rationale:** Delivers the no-install access requirement EPC-009 identifies as a stated differentiator over conventional tools - a user must be able to go from zero to a rendered diagram in a single browser session with no preceding setup.

---

## EPC-009-US-002 - Process map produced without creating or logging into an account

As a business analyst, I want to produce and view a process map without creating an account or logging in, so that I can evaluate the tool's value before committing to any registration step.

**Acceptance criteria:**

**Scenario 1: Full map generation available without account creation**
Given I have not created an account or provided any credentials, when I navigate to the tool and submit a process description, then the system processes my input and renders a complete process map without redirecting me to a registration or sign-in step.

**Scenario 2: Account creation is offered but not required to proceed**
Given I have just received a rendered process map without signing in, when the tool presents an option to save or create an account, then I can dismiss or ignore that option and continue using the tool for the current session without the session being blocked or degraded.

**Scenario 3: Map functionality is not reduced for unauthenticated users within session scope**
Given I am using the tool without an account during a single session, when I edit my process map and export it, then I have access to the same generation, editing, and export capabilities as an account holder - except for capabilities that are explicitly described as account-only features.

**Scenario 4: Unauthenticated session does not require personal information to begin**
Given I arrive at the tool for the first time with no account, when I begin a session, then the tool does not require me to provide an email address, name, or any other personal information before I can submit a process description.

**Rationale:** Delivers the no-mandatory-account access requirement EPC-009 identifies as central to frictionless evaluation - a user must be able to reach full map-generation value before any account or registration gate is encountered.

---

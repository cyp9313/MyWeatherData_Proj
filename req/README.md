# Requirements Engineering – MyWeatherData

Dieser Ordner enthält alle Anforderungen des Projekts, strukturiert in drei Ebenen:

```
req/
├── epic/                      # Epics (große, übergeordnete Themenblöcke)
├── user-story/                # User Stories (nutzerorientierte Anforderungen je Epic)
└── functional-requirement/    # Functional Requirements (konkrete, testbare Anforderungen je User Story)
```

## Hierarchie & Traceability

```
Epic (EPIC-xxx)
 └── User Story (US-xxx)
      └── Functional Requirement (FR-xxx)
```

Jede Ebene referenziert ihre übergeordnete Ebene über die ID (siehe Feld "Parent" bzw. "Zugehörige Epic/User Story" in den Templates). Dadurch bleibt jederzeit nachvollziehbar, welches Requirement zu welcher Story bzw. welchem Epic gehört.

## ID-Konventionen

| Ebene                  | Präfix | Beispiel  | Dateiname                              |
|------------------------|--------|-----------|-----------------------------------------|
| Epic                   | EPIC-  | EPIC-001  | `epic/EPIC-001-kurztitel.md`             |
| User Story             | US-    | US-001    | `user-story/US-001-kurztitel.md`         |
| Functional Requirement | FR-    | FR-001    | `functional-requirement/FR-001-kurztitel.md` |

- IDs werden fortlaufend und projektweit eindeutig vergeben (keine erneute Verwendung nach Löschung).
- Dateinamen: `<ID>-<kurzer-sprechender-titel-in-kleinbuchstaben-mit-bindestrichen>.md`

## Vorgehen beim Anlegen neuer Anforderungen

1. Passendes Template aus dem jeweiligen Ordner kopieren (`TEMPLATE-*.md`).
2. Datei gemäß Namenskonvention umbenennen und nächste freie ID vergeben.
3. Alle Platzhalter (`<...>`) ausfüllen.
4. Verknüpfung zur übergeordneten Ebene (Parent-ID) eintragen.
5. Status pflegen (Draft → Review → Approved → Done).

## Status-Werte

`Draft` · `Review` · `Approved` · `In Arbeit` · `Done` · `Verworfen`

## Priorisierung (MoSCoW)

`Must have` · `Should have` · `Could have` · `Won't have`

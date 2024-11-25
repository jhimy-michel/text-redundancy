from text_analyzer import TextAnalyzer


test_text = """
Aktueller Status und Verlauf seit letzter Sitzung:

- Erinnerungen an ein früheres Erlebnis sind weniger belastend geworden. Sie werden nicht mehr als überwältigend empfunden, sondern eher als träumerisch und teilweise positiv.
- Auf einer Belastungsskala von 0 bis 10 werden die Erinnerungen als weniger belastend wahrgenommen. Sie sind nicht mehr so präsent und überwältigend.
- Medikamente scheinen noch nicht vollständig zu wirken; weitere Anpassungen werden erwogen. Es besteht Unsicherheit, ob die Medikamente die gewünschte Wirkung erzielen, und Anpassungen werden in Betracht gezogen.
- Der Wohnort in der Nähe eines Spitals löst gelegentlich Erinnerungen aus, die jedoch nicht mehr stark belastend sind. Beim Vorbeigehen an das Spital werden Erinnerungen an die Vergangenheit wachgerufen, aber sie sind nicht mehr so präsent und belastend.
- In den letzten zwei Wochen hat sich die Panikstörung verschlechtert, obwohl es zuvor besser war. Es treten vermehrt Schwindelgefühle und ein Engegefühl auf, die jedoch keine Panikattacke auslösen.
- Im Alltag gibt es keine Einschränkungen, aber es kostet viel Energie. Der Alltag ist machbar, erfordert jedoch viel Energie zur Bewältigung der Symptome.

Anliegen für die heutige Stunde:

- Hauptthema: Umgang mit Panikstörungen und der Angst vor zukünftigen Belastungen. Es besteht Sorge, dass die Panikstörung in Zukunft wieder auftreten könnte, insbesondere in stressigen Zeiten.
- Besprochene Problemstellung: Die Balance zwischen Ruhe und Aktivität finden, um Panikattacken zu vermeiden. Es soll gelernt werden, besser auf sich selbst zu achten, um Panikattacken zu verhindern.

Sitzungsverlauf:

- Diskussion über die Belastung durch Erinnerungen und die Möglichkeit, diese zu verarbeiten. Es wird reflektiert, wie sich die Wahrnehmung der Erinnerungen verändert hat und sie weniger belastend empfunden werden.
- Der Vorschlag, die Aufmerksamkeit auf den Körper und die eigenen Bedürfnisse zu lenken (Achtsamkeit). Die Bedeutung, auf die Signale des Körpers zu achten und Achtsamkeit in den Alltag zu integrieren, wird besprochen.
- Der Wunsch, mehr auf sich selbst zu achten und weniger zu funktionieren, wird geäußert. Es wird erkannt, dass oft das Bedürfnis besteht, zu funktionieren, und es soll gelernt werden, mehr auf sich selbst zu achten.
- Metaphern (z.B. Pfosten beim Velofahren) werden zur Veranschaulichung der Problematik verwendet. Die Metapher verdeutlicht, wie wichtig es ist, den Fokus nicht auf die Angst zu richten, sondern auf die positiven Aspekte des Lebens.
- Interesse an Achtsamkeitsübungen und die Notwendigkeit, sich selbst besser wahrzunehmen, werden erkannt. Es besteht Interesse daran, Achtsamkeitsübungen auszuprobieren, um sich selbst besser wahrzunehmen.
- Ermutigung, regelmäßig kurze Momente der Selbstwahrnehmung einzubauen. Es wird empfohlen, regelmäßig kurze Momente der Achtsamkeit in den Alltag zu integrieren, um die Selbstwahrnehmung zu stärken.

Bis zur nächsten Sitzung:

- Achtsamkeitsübungen sollen in den Alltag integriert werden, um besser auf sich selbst zu achten. Es soll gelernt werden, wie Achtsamkeit in den Alltag eingebaut werden kann, um die Symptome besser zu bewältigen.
- Ziel ist es, die Balance zwischen Aktivität und Ruhe zu finden, um Panikattacken zu vermeiden. Eine Balance zwischen Aktivität und Ruhe soll gefunden werden, um Panikattacken zu verhindern.
- Die Unterstützung des sozialen Umfelds soll genutzt werden, um mehr Ruhe zu finden. Die Unterstützung des sozialen Umfelds soll genutzt werden, um mehr Ruhe in den Alltag zu integrieren.

Zusätzliches:

- Es besteht die Befürchtung, dass zukünftige Belastungen, wie eine erneute Schwangerschaft, die Panikstörung wieder verstärken könnten. Erfahrungen in der ersten Schwangerschaft und die damit verbundenen Ängste werden reflektiert.
- Es wird über die Bedeutung von Selbstfürsorge und die Herausforderung, sich selbst Ruhe zu gönnen, gesprochen. Es wird erkannt, dass oft das Bedürfnis besteht, zu funktionieren, und es soll gelernt werden, sich selbst mehr Ruhe zu gönnen.
- Interesse daran, neue Wege zu finden, um sich selbst besser wahrzunehmen und auf sich zu achten, wird gezeigt. Es soll gelernt werden, wie Achtsamkeit in den Alltag integriert werden kann, um die Symptome besser zu bewältigen.
- Es wird über die Bedeutung von Achtsamkeit und Selbstwahrnehmung gesprochen und wie diese helfen können, die Symptome der Panikstörung zu bewältigen. Interesse daran, Achtsamkeitsübungen auszuprobieren, um sich selbst besser wahrzunehmen, wird gezeigt.

    """

if __name__ == "__main__":
    
    
    # Initialize and analyze
    analyzer = TextAnalyzer()
    redundancies = analyzer.find_redundancies(test_text)
    
    if not redundancies:
        print("\nNo redundancies found!")
    else:
        print("\nRedundancy Analysis:")
        print("===================")
        
        for i, group in enumerate(redundancies, 1):
            print(f"\nRedundancy Group {i}:")
            print(f"Section: {group['section']}")
            print(f"Main point: {group['main_point']}")
            print("\nSimilar points:")
            for point in group['similar_points']:
                print(f"Similarity {point['similarity']:.3f}:")
                print(f"- {point['text']}")
                print()
# 🤖 Multi-Agent Customer Support with Agno and Mistral

Ce projet implémente un système **multi-agent** utilisant la librairie **Agno** (v1.8.0) et le modèle **Mistral** via son API.  
L’objectif est d’automatiser le traitement des tickets clients :  
➡️ un agent analyse le problème signalé,  
➡️ un autre rédige une réponse claire et professionnelle.

---

## ✨ Fonctionnalités

- 🧩 **Analyst Agent** : analyse le message du client et identifie le problème principal.  
- 💬 **Response Agent** : rédige une réponse claire, polie et adaptée au contexte du ticket.  
- 🤝 **Team Coordination** : orchestre la collaboration entre les deux agents pour produire une réponse cohérente.  
- ⚙️ **Utilisation de MistralChat** pour la génération de texte naturelle et fluide.  
- 🔐 **Gestion sécurisée de la clé API** via `.env`.

---
## 💻 Exemple d’exécution

Lorsqu’un client écrit :
> "Je n'arrive pas à finaliser mon paiement sur le site."
Le système produit :  
![Exécution du système](./images/image.png)



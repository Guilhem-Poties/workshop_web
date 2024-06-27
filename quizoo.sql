-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8889
-- Généré le : jeu. 27 juin 2024 à 10:45
-- Version du serveur :  5.7.34
-- Version de PHP : 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `quizoo`
--

-- --------------------------------------------------------

--
-- Structure de la table `question`
--

CREATE TABLE `question` (
  `id_question` int(11) NOT NULL,
  `libelle` varchar(100) NOT NULL,
  `id_theme` int(11) NOT NULL,
  `id_bonne_reponse` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Déchargement des données de la table `question`
--

INSERT INTO `question` (`id_question`, `libelle`, `id_theme`, `id_bonne_reponse`) VALUES
(0, 'Que produisent les vaches ?', 0, 0),
(1, 'Les moutons sont ?', 0, 4),
(2, 'Comment s’appelle le petit de la poule ?', 0, 7),
(3, 'Quel animal dort debout ?', 0, 11),
(4, 'Quel animal est le plus intelligent à la ferme ?', 0, 12),
(5, 'Combien de plumes ont les pigeons?', 1, 15),
(6, 'Quel est le plus grand oiseau du Monde?', 1, 18),
(7, 'Combien de mots peut comprendre un perroquet?', 1, 23),
(8, 'De quelles couleurs est le martin-pêcheur ?', 1, 25),
(9, 'Qui sont les oiseaux les plus petits du Monde ?', 1, 29),
(10, 'Combien pèse une girafe à la naissance ?', 2, 30),
(11, 'Que mange le rhinocéros ?', 2, 33),
(12, 'Quel est la période de gestation de l\'éléphant ?', 2, 37),
(13, 'Quel animal court le plus vite ?', 2, 40),
(14, 'Les lions ont plus de chances d\'attirer une femelle si leur crinière est foncée ?', 2, 42);

-- --------------------------------------------------------

--
-- Structure de la table `reponse`
--

CREATE TABLE `reponse` (
  `id` int(11) NOT NULL,
  `libelle` varchar(50) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `id_question` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Déchargement des données de la table `reponse`
--

INSERT INTO `reponse` (`id`, `libelle`, `image`, `id_question`) VALUES
(0, 'Du lait', NULL, 0),
(1, 'Du fromage', NULL, 0),
(2, 'Des oeufs', NULL, 0),
(3, 'Carnivore', NULL, 1),
(4, 'Herbivore', NULL, 1),
(5, 'Omnivore', NULL, 1),
(6, 'Le veau', NULL, 2),
(7, 'Le poussin', NULL, 2),
(8, 'Le coq', NULL, 2),
(9, 'Le chien', NULL, 3),
(10, 'La poule', NULL, 3),
(11, 'Le cheval', NULL, 3),
(12, 'Le cochon', NULL, 4),
(13, 'Le coq', NULL, 4),
(14, 'Le lapin', NULL, 4),
(15, '10 000 plumes', NULL, 5),
(16, '7 000 plumes', NULL, 5),
(17, '5 000 plumes', NULL, 5),
(18, 'L\'autruche', NULL, 6),
(19, 'L\'aigle royal', NULL, 6),
(20, 'Le marabout d\'Afrique', NULL, 6),
(21, '10 mots', NULL, 7),
(22, '100 mots', NULL, 7),
(23, '1 000 mots', NULL, 7),
(24, 'Vert et jaune', NULL, 8),
(25, 'Bleu et orange', NULL, 8),
(26, 'Rouge et noir', NULL, 8),
(27, 'Les pigeons', NULL, 9),
(28, 'Les moineaux', NULL, 9),
(29, 'Les colibris', NULL, 9),
(30, 'Entre 40 et 80 kilos', NULL, 10),
(31, 'Entre 80 et 120 kilos', NULL, 10),
(32, 'Entre 120 et 160 kilos', NULL, 10),
(33, 'Des plantes', NULL, 11),
(34, 'De la viande', NULL, 11),
(35, 'Du poisson', NULL, 11),
(36, '9 mois', NULL, 12),
(37, '21 mois', NULL, 12),
(38, '15 mois', NULL, 12),
(39, 'Le leopard ', NULL, 13),
(40, 'Le guépard ', NULL, 13),
(41, 'Le lion', NULL, 13),
(42, 'Vrai', NULL, 14),
(43, 'Faux', NULL, 14),
(44, 'Je ne sais pas', NULL, 14);

-- --------------------------------------------------------

--
-- Structure de la table `session`
--

CREATE TABLE `session` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `score` int(11) NOT NULL,
  `id_user` int(11) NOT NULL,
  `id_theme` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

-- --------------------------------------------------------

--
-- Structure de la table `theme`
--

CREATE TABLE `theme` (
  `id` int(11) NOT NULL,
  `libelle` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Déchargement des données de la table `theme`
--

INSERT INTO `theme` (`id`, `libelle`, `description`) VALUES
(0, 'Les animaux de la ferme', 'Devient incollable sur la vache le coq et leurs amis!'),
(1, 'Les oiseaux', 'Teste toi sur les animaux volants!'),
(2, 'Safari', 'Apprend tout sur les animaux de la Savane!');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `id` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `date_naissance` date NOT NULL,
  `mdp` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `question`
--
ALTER TABLE `question`
  ADD PRIMARY KEY (`id_question`),
  ADD UNIQUE KEY `id_bonne_reponse` (`id_bonne_reponse`),
  ADD KEY `id_theme` (`id_theme`) USING BTREE;

--
-- Index pour la table `reponse`
--
ALTER TABLE `reponse`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_question` (`id_question`) USING BTREE;

--
-- Index pour la table `session`
--
ALTER TABLE `session`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_user` (`id_user`),
  ADD UNIQUE KEY `id_theme` (`id_theme`);

--
-- Index pour la table `theme`
--
ALTER TABLE `theme`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `utilisateur`
--
ALTER TABLE `utilisateur`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `question`
--
ALTER TABLE `question`
  ADD CONSTRAINT `question_ibfk_1` FOREIGN KEY (`id_theme`) REFERENCES `theme` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `question_ibfk_2` FOREIGN KEY (`id_bonne_reponse`) REFERENCES `reponse` (`id`) ON DELETE SET NULL ON UPDATE SET NULL;

--
-- Contraintes pour la table `reponse`
--
ALTER TABLE `reponse`
  ADD CONSTRAINT `reponse_ibfk_1` FOREIGN KEY (`id_question`) REFERENCES `question` (`id_question`) ON UPDATE CASCADE;

--
-- Contraintes pour la table `session`
--
ALTER TABLE `session`
  ADD CONSTRAINT `session_ibfk_1` FOREIGN KEY (`id_theme`) REFERENCES `theme` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `session_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `utilisateur` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

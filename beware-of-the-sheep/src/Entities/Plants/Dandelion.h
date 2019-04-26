#pragma once
#include "Plant.h"

namespace bots {

	/*!
		\brief
		\author	Konstanty Misiak
	*/
	class Dandelion :
		public Plant
	{
	public:
		Dandelion(World & world, const Point & position);
		virtual ~Dandelion() = default;

		void action() override;
	protected:
		inline std::string getSymbol() const override { return "DN"; }
		inline Kind getKind() const override { return Kind::Dandelion; }
		inline std::string getClassName() const override { return "Dandelion"; }
	private:

	};

} // namespace bots
